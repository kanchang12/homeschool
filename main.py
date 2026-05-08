from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import os, base64, httpx, psycopg2, psycopg2.extras
from contextlib import contextmanager
from google import genai
from google.genai import types
from tasks import TASKS, get_task

# ── DB ────────────────────────────────────────────────────────────────────────
DATABASE_URL = os.getenv("DATABASE_URL")

@contextmanager
def get_db():
    conn = psycopg2.connect(DATABASE_URL)
    conn.autocommit = False
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

def init_db():
    with get_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password TEXT NOT NULL,
                    role     TEXT NOT NULL,
                    name     TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS progress (
                    id          SERIAL PRIMARY KEY,
                    username    TEXT NOT NULL,
                    role        TEXT NOT NULL,
                    task_id     INTEGER NOT NULL,
                    completed   BOOLEAN NOT NULL DEFAULT FALSE,
                    attempts    INTEGER NOT NULL DEFAULT 0,
                    last_input  TEXT DEFAULT '',
                    last_output TEXT DEFAULT '',
                    updated_at  TIMESTAMP DEFAULT NOW(),
                    UNIQUE(username, task_id)
                );
            """)
            cur.execute("SELECT COUNT(*) FROM users")
            if cur.fetchone()[0] == 0:
                cur.executemany(
                    "INSERT INTO users (username, password, role, name) VALUES (%s,%s,%s,%s)",
                    [
                        ("kid",   "learn123", "kid",   "Kid"),
                        ("adult", "learn123", "adult", "Adult"),
                        ("admin", "admin123", "adult", "Admin"),
                    ]
                )

# ── App ───────────────────────────────────────────────────────────────────────
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.mount("/static", StaticFiles(directory="static"), name="static")

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY", ""))

@app.on_event("startup")
def startup():
    init_db()

# ── Auth ──────────────────────────────────────────────────────────────────────
class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/api/login")
def login(req: LoginRequest):
    with get_db() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute("SELECT * FROM users WHERE username = %s", (req.username.lower(),))
            user = cur.fetchone()
    if not user or user["password"] != req.password:
        raise HTTPException(status_code=401, detail="Wrong username or password")
    return {"username": user["username"], "role": user["role"], "name": user["name"]}

# ── Tasks ─────────────────────────────────────────────────────────────────────
@app.get("/api/tasks/{role}")
def get_tasks(role: str):
    if role not in TASKS:
        raise HTTPException(status_code=404, detail="Role not found")
    return {"tasks": TASKS[role], "total": len(TASKS[role])}

@app.get("/api/tasks/{role}/{task_id}")
def get_single_task(role: str, task_id: int):
    task = get_task(role, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# ── Progress ──────────────────────────────────────────────────────────────────
class ProgressRequest(BaseModel):
    username: str
    role: str
    task_id: int
    completed: bool = False
    last_input: str = ""
    last_output: str = ""

@app.post("/api/progress")
def save_progress(req: ProgressRequest):
    with get_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO progress (username, role, task_id, completed, attempts, last_input, last_output, updated_at)
                VALUES (%s, %s, %s, %s, 1, %s, %s, NOW())
                ON CONFLICT (username, task_id) DO UPDATE SET
                    completed   = GREATEST(progress.completed::int, EXCLUDED.completed::int)::boolean,
                    attempts    = progress.attempts + 1,
                    last_input  = EXCLUDED.last_input,
                    last_output = EXCLUDED.last_output,
                    updated_at  = NOW()
            """, (req.username, req.role, req.task_id, req.completed, req.last_input[:1000], req.last_output[:1000]))
    return {"saved": True}

@app.get("/api/progress/{username}")
def get_progress(username: str):
    with get_db() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(
                "SELECT task_id, completed, attempts, last_input, last_output, updated_at FROM progress WHERE username = %s ORDER BY task_id",
                (username,)
            )
            rows = cur.fetchall()
    return {
        "username": username,
        "progress": [dict(r) for r in rows],
        "completed_count": sum(1 for r in rows if r["completed"]),
        "total_attempts": sum(r["attempts"] for r in rows),
    }

@app.delete("/api/progress/{username}")
def reset_progress(username: str):
    with get_db() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM progress WHERE username = %s", (username,))
    return {"reset": True}

# ── Shared Gemini text helper ─────────────────────────────────────────────────
def gemini_text(system: str, messages: list, temperature: float = 0.7, max_tokens: int = 1500) -> str:
    contents = []
    for m in messages:
        role = "user" if m["role"] == "user" else "model"
        contents.append(types.Content(role=role, parts=[types.Part(text=m["content"])]))
    config = types.GenerateContentConfig(
        temperature=temperature,
        max_output_tokens=max_tokens,
        system_instruction=system or None,
    )
    response = client.models.generate_content(model="gemini-2.0-flash", contents=contents, config=config)
    return response.text

# ── Text / LLM ────────────────────────────────────────────────────────────────
class TextRequest(BaseModel):
    instruction: str
    input: str = ""
    temperature: float = 0.7

@app.post("/api/run/text")
def run_text(req: TextRequest):
    content = req.instruction
    if req.input.strip():
        content += "\n\n" + req.input
    text = gemini_text("", [{"role": "user", "content": content}], req.temperature, 1500)
    return {"text": text}

# ── Image Generation ──────────────────────────────────────────────────────────
class ImageRequest(BaseModel):
    prompt: str

@app.post("/api/run/image")
def run_image(req: ImageRequest):
    try:
        response = client.models.generate_images(
            model="imagen-3.0-generate-002",
            prompt=req.prompt,
            config=types.GenerateImagesConfig(number_of_images=1, aspect_ratio="1:1")
        )
        img = response.generated_images[0]
        b64 = base64.b64encode(img.image.image_bytes).decode("utf-8")
        return {"image_b64": b64, "mime_type": "image/png"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ── Vision ────────────────────────────────────────────────────────────────────
class VisionRequest(BaseModel):
    instruction: str
    image_url: str

@app.post("/api/run/vision")
async def run_vision(req: VisionRequest):
    try:
        async with httpx.AsyncClient(timeout=15) as http:
            r = await http.get(req.image_url)
            if r.status_code != 200:
                raise HTTPException(status_code=400, detail="Could not fetch image URL")
            image_bytes = r.content
            mime_type = r.headers.get("content-type", "image/jpeg").split(";")[0]

        contents = [
            types.Content(role="user", parts=[
                types.Part(inline_data=types.Blob(mime_type=mime_type, data=image_bytes)),
                types.Part(text=req.instruction)
            ])
        ]
        config = types.GenerateContentConfig(max_output_tokens=1000)
        response = client.models.generate_content(model="gemini-2.0-flash", contents=contents, config=config)
        return {"text": response.text}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ── RAG ───────────────────────────────────────────────────────────────────────
class RAGRequest(BaseModel):
    question: str
    document: str

@app.post("/api/run/rag")
def run_rag(req: RAGRequest):
    system = (
        "You are a precise document analyst. Answer questions based ONLY on the provided document. "
        "If the answer is not in the document, say exactly: 'This information is not in the provided document.' "
        "Quote the relevant section when you answer."
    )
    content = f"DOCUMENT:\n{req.document}\n\nQUESTION:\n{req.question}"
    text = gemini_text(system, [{"role": "user", "content": content}], 0.2, 1000)
    return {"text": text}

# ── Chatbot ───────────────────────────────────────────────────────────────────
class ChatbotRequest(BaseModel):
    system_prompt: str
    messages: List[dict]

@app.post("/api/run/chatbot")
def run_chatbot(req: ChatbotRequest):
    text = gemini_text(req.system_prompt, req.messages, 0.8, 800)
    return {"text": text}

# ── Tutor (AI tutor sidebar) ──────────────────────────────────────────────────
class TutorRequest(BaseModel):
    role: str
    task_id: int
    messages: List[dict]
    current_instruction: str = ""
    current_input: str = ""
    last_output: str = ""

@app.post("/api/tutor")
def tutor(req: TutorRequest):
    task = get_task(req.role, req.task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if req.role == "kid":
        system = (
            f"You are CodeBuddy, a fun encouraging coding tutor for children. "
            f"Current task: \"{task['title']}\" — {task['desc']}. "
            f"Hints available: {'; '.join(task['hints'])}. "
            f"Short fun replies with emojis. Give hints only, never the full answer."
        )
    else:
        system = (
            f"You are an expert AI tutor helping adults learn practical AI skills. "
            f"Current task: \"{task['title']}\" — {task['desc']}. "
            f"Task type: {task.get('task_type','text')}. "
            f"The learner's current instruction: {req.current_instruction[:200] or 'not written yet'}. "
            f"Last output they got: {req.last_output[:200] or 'nothing yet'}. "
            f"Hints: {'; '.join(task['hints'])}. "
            f"Be concise. Guide them to improve their prompt or approach. Never write the answer for them."
        )
    text = gemini_text(system, req.messages, 0.7, 400)
    return {"text": text}

# ── Legacy LLM endpoint (keep for backwards compat) ──────────────────────────
class LLMRequest(BaseModel):
    model: str = "gemini-2.0-flash"
    system: Optional[str] = None
    messages: List[dict]
    temperature: float = 0.7
    max_tokens: int = 500

@app.post("/api/llm")
def call_llm(req: LLMRequest):
    text = gemini_text(req.system or "", req.messages, req.temperature, req.max_tokens)
    return {"text": text}

# ── Static ────────────────────────────────────────────────────────────────────
@app.get("/", response_class=HTMLResponse)
def index():
    return FileResponse("static/index.html")

@app.get("/{path:path}", response_class=HTMLResponse)
def catch_all(path: str):
    return FileResponse("static/index.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", 8080)), reload=False)
