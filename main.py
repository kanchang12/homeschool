from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import os
import psycopg2
import psycopg2.extras
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
                    last_canvas TEXT DEFAULT '',
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
    canvas_blocks: List[str] = []
    last_output: str = ""

@app.post("/api/progress")
def save_progress(req: ProgressRequest):
    with get_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO progress (username, role, task_id, completed, attempts, last_canvas, last_output, updated_at)
                VALUES (%s, %s, %s, %s, 1, %s, %s, NOW())
                ON CONFLICT (username, task_id) DO UPDATE SET
                    completed   = GREATEST(progress.completed::int, EXCLUDED.completed::int)::boolean,
                    attempts    = progress.attempts + 1,
                    last_canvas = EXCLUDED.last_canvas,
                    last_output = EXCLUDED.last_output,
                    updated_at  = NOW()
            """, (req.username, req.role, req.task_id, req.completed, ",".join(req.canvas_blocks), req.last_output[:500]))
    return {"saved": True}

@app.get("/api/progress/{username}")
def get_progress(username: str):
    with get_db() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(
                "SELECT task_id, completed, attempts, last_canvas, last_output, updated_at FROM progress WHERE username = %s ORDER BY task_id",
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

# ── LLM ───────────────────────────────────────────────────────────────────────
def gemini_call(model, system, messages, temperature, max_tokens):
    contents = []
    for m in messages:
        role = "user" if m["role"] == "user" else "model"
        contents.append(types.Content(role=role, parts=[types.Part(text=m["content"])]))
    config = types.GenerateContentConfig(
        temperature=temperature,
        max_output_tokens=max_tokens,
        system_instruction=system or None,
    )
    response = client.models.generate_content(model=model, contents=contents, config=config)
    return response.text

class LLMRequest(BaseModel):
    model: str = "gemini-2.0-flash"
    system: Optional[str] = None
    messages: List[dict]
    temperature: float = 0.7
    max_tokens: int = 500

@app.post("/api/llm")
def call_llm(req: LLMRequest):
    text = gemini_call(req.model, req.system, req.messages, req.temperature, req.max_tokens)
    return {"text": text}

class TutorRequest(BaseModel):
    role: str
    task_id: int
    messages: List[dict]
    canvas_blocks: List[str] = []
    last_output: str = ""

@app.post("/api/tutor")
def tutor(req: TutorRequest):
    task = get_task(req.role, req.task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if req.role == "kid":
        system = (
            f"You are CodeBuddy, a fun encouraging tutor for children learning Python through visual blocks. "
            f"Current task: \"{task['title']}\" — {task['desc']}. "
            f"Hints: {'; '.join(task['hints'])}. "
            f"Blocks on canvas: {', '.join(req.canvas_blocks) or 'none'}. "
            f"Last output: {req.last_output[:100] or 'none'}. "
            f"Short fun replies with emojis. Give hints, never full answers."
        )
    else:
        system = (
            f"You are an expert AI engineering tutor teaching adults to build LLM pipelines using blocks. "
            f"Current task: \"{task['title']}\" — {task['desc']}. "
            f"Hints: {'; '.join(task['hints'])}. "
            f"Blocks on canvas: {', '.join(req.canvas_blocks) or 'none'}. "
            f"Last output: {req.last_output[:100] or 'none'}. "
            f"Be concise. Give hints, not full solutions."
        )
    text = gemini_call("gemini-2.0-flash", system, req.messages, 0.7, 300)
    return {"text": text}

# ── Static ────────────────────────────────────────────────────────────────────
@app.get("/", response_class=HTMLResponse)
def index():
    return FileResponse("static/index.html")

@app.get("/{path:path}", response_class=HTMLResponse)
def catch_all(path: str):
    return FileResponse("static/index.html")

# ── Entrypoint ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", 8080)), reload=False)
