# tasks.py

TASKS = {
    "kid": [
        {"id":1,"title":"Hello Print","desc":"Print 'Hello, AI!' to screen","hints":["Use print()","Wrap text in quotes","Check spelling"],"success_keys":["print","hello"],"cat":"coding"},
        {"id":2,"title":"Asterisk Line","desc":"Print ***** using string multiplication","hints":["Use '*'","Multiply by 5","Print result"],"success_keys":["print","*","5"],"cat":"coding"},
        {"id":3,"title":"Number Counter","desc":"Print 1 to 5 using a loop","hints":["Use for loop","range(1,6)","print(i)"],"success_keys":["for","range","print"],"cat":"coding"},
        {"id":4,"title":"Asterisk Triangle","desc":"Print right triangle of * height 4","hints":["Loop 1-4","'*' * i inside loop","print each line"],"success_keys":["for","range","*","print"],"cat":"coding"},
        {"id":5,"title":"Sum Two Numbers","desc":"Add 12 + 34 and print","hints":["Use + operator","Store in variable","print result"],"success_keys":["+","print","="],"cat":"math"},
        {"id":6,"title":"Even/Odd Checker","desc":"Check if 7 is even or odd","hints":["Use % operator","if num%2==0","else print odd"],"success_keys":["%","if","else","print"],"cat":"math"},
        {"id":7,"title":"Leap Year Logic","desc":"Check if 2024 is leap year","hints":["divisible by 4","not by 100 unless by 400","if/elif chain"],"success_keys":["if","%","and","or"],"cat":"science"},
        {"id":8,"title":"Count Vowels","desc":"Count vowels in 'education'","hints":["loop through string","check in 'aeiou'","counter+=1"],"success_keys":["for","in","if","counter"],"cat":"english"},
        {"id":9,"title":"Reverse Word","desc":"Reverse 'python' using slicing","hints":["use [::-1]","store in var","print it"],"success_keys":["[::-1]","print"],"cat":"coding"},
        {"id":10,"title":"Average Calculator","desc":"Find avg of 10,20,30","hints":["sum them","divide by 3","use ()"],"success_keys":["+","/","print"],"cat":"math"},
        {"id":11,"title":"FizzBuzz Lite","desc":"Print 1-10, replace 3 with Fizz, 5 with Buzz","hints":["loop 1-10","if i%3==0","elif i%5==0"],"success_keys":["for","if","%","print"],"cat":"coding"},
        {"id":12,"title":"Max in List","desc":"Find max in [4,9,2,7]","hints":["use max()","or loop compare","track highest"],"success_keys":["max","or","for","if"],"cat":"math"},
        {"id":13,"title":"Word Count","desc":"Count words in 'I love AI coding'","hints":["split string","len()","print count"],"success_keys":["split","len","print"],"cat":"english"},
        {"id":14,"title":"Case Swap","desc":"Convert 'Hello' to 'hELLO'","hints":["swapcase()","or loop char by char","print"],"success_keys":["swapcase","or","print"],"cat":"english"},
        {"id":15,"title":"Factorial","desc":"Calculate 5! (120)","hints":["start result=1","loop 1-5","result*=i"],"success_keys":["for","*=","print"],"cat":"math"},
        {"id":16,"title":"Palindrome Check","desc":"Check if 'racecar' reads same backwards","hints":["reverse string","compare ==","if/else"],"success_keys":["[::-1]","==","if"],"cat":"coding"},
        {"id":17,"title":"Grade Calculator","desc":"Print A/B/C/D based on score >=90/80/70/60","hints":["if/elif chain","score>=90","print letter"],"success_keys":["if","elif","print"],"cat":"math"},
        {"id":18,"title":"Sum Digits","desc":"Sum digits of 1234","hints":["convert to str","loop chars","int(char) add"],"success_keys":["for","int","+","sum"],"cat":"math"},
        {"id":19,"title":"Prime Check","desc":"Check if 17 is prime","hints":["loop 2 to num-1","if num%i==0 return False","else True"],"success_keys":["for","%","if","return"],"cat":"math"},
        {"id":20,"title":"List Filter","desc":"Keep only numbers >5 from [2,7,1,9,3]","hints":["new list=[]","for n in list","if n>5 append"],"success_keys":["for","if","append"],"cat":"coding"},
        {"id":21,"title":"Temperature Convert","desc":"Convert 32°C to °F (formula: *9/5+32)","hints":["multiply 9/5","add 32","print result"],"success_keys":["*","/","+","print"],"cat":"science"},
        {"id":22,"title":"Fibonacci Lite","desc":"Print first 6 Fibonacci numbers","hints":["a=0,b=1","loop 6 times","print a, a,b=b,a+b"],"success_keys":["for","a,b","print"],"cat":"math"},
        {"id":23,"title":"String Replace","desc":"Replace 'cat' with 'dog' in string","hints":["use .replace()","print new string"],"success_keys":["replace","print"],"cat":"english"},
        {"id":24,"title":"Guess Number Logic","desc":"Simulate: if guess==7 print win, else try again","hints":["if guess==7","print win","else print try"],"success_keys":["if","==","print","else"],"cat":"coding"},
        {"id":25,"title":"Matrix Row Sum","desc":"Sum first row of [[1,2],[3,4]]","hints":["row[0]","sum()","print"],"success_keys":["sum","print"],"cat":"math"},
        {"id":26,"title":"Alphabet Order","desc":"Check if letters in 'ace' are ascending","hints":["list()","== sorted()","if/else"],"success_keys":["sorted","==","if"],"cat":"english"},
        {"id":27,"title":"Gravity Calc","desc":"Calculate distance: 0.5*9.8*t^2 for t=3","hints":["use ** for power","0.5*9.8*t**2","print"],"success_keys":["*","**","print"],"cat":"science"},
        {"id":28,"title":"Frequency Counter","desc":"Count 'a' in 'banana'","hints":[".count()","or loop","print"],"success_keys":["count","or","for","print"],"cat":"english"},
        {"id":29,"title":"Tic-Tac-Toe Grid","desc":"Print 3x3 grid using nested loops","hints":["for i in range(3)","for j in range(3)","print end=''"],"success_keys":["for","range","print"],"cat":"coding"},
        {"id":30,"title":"Story Generator","desc":"Combine name, place, action into sentence","hints":["f-strings","f'{name} went to {place}'","print"],"success_keys":["f'","print"],"cat":"english"},
    ],

    "adult": [
        # ── WEEK 1: Text AI ──────────────────────────────────────────────────
        {
            "id":1,"title":"Your First Prompt","cat":"text",
            "desc":"Ask Gemini: 'What is artificial intelligence in simple words?' — See how it responds. Then improve your prompt to get a shorter, clearer answer.",
            "hints":["A good prompt is specific","Try adding: 'Explain in 2 sentences'","Try adding: 'for a 10-year-old'"],
            "task_type":"text","tool":"llm",
            "starter_instruction":"What is artificial intelligence in simple words?",
            "starter_input":""
        },
        {
            "id":2,"title":"Prompt Engineering","cat":"text",
            "desc":"The same question, three different prompts — see how the output changes. Add a role ('You are a teacher'), a format ('use bullet points'), and a constraint ('max 50 words').",
            "hints":["Start with: 'You are a...'","Add format instructions","Add length constraints"],
            "task_type":"text","tool":"llm",
            "starter_instruction":"You are a friendly teacher. Explain machine learning in 3 bullet points, max 50 words total.",
            "starter_input":""
        },
        {
            "id":3,"title":"Summarise Any Text","cat":"text",
            "desc":"Paste any article or long text. Ask AI to summarise it in 3 bullet points. This is one of the most useful things AI does in real work.",
            "hints":["Paste text in the Input box","Tell AI the format you want","Try: 'Summarise in 3 bullets with a one-line TL;DR at the top'"],
            "task_type":"text","tool":"llm",
            "starter_instruction":"Summarise the following text in 3 bullet points with a one-line TL;DR at the top.\n\nText:",
            "starter_input":"Artificial intelligence (AI) is rapidly transforming industries worldwide. From healthcare to finance, AI systems are automating tasks, improving decisions, and creating new possibilities. Machine learning, a subset of AI, enables computers to learn from data without being explicitly programmed. Deep learning, using neural networks, has driven breakthroughs in image recognition, language understanding, and game playing. However, AI also raises important questions about jobs, privacy, and ethical use of technology."
        },
        {
            "id":4,"title":"Tone Rewriter","cat":"text",
            "desc":"Take one piece of text and rewrite it in 3 different tones: formal, casual, and persuasive. This is how copywriters and marketers use AI every day.",
            "hints":["Give AI the original text","Ask for 3 versions labeled clearly","Try it with an email, a job posting, or a product description"],
            "task_type":"text","tool":"llm",
            "starter_instruction":"Rewrite the following text in three tones:\n1. Formal (for a business report)\n2. Casual (for a WhatsApp message)\n3. Persuasive (for a sales pitch)\n\nLabel each version clearly.\n\nText:",
            "starter_input":"We are launching a new app that helps people learn AI skills through hands-on practice."
        },
        {
            "id":5,"title":"Extract Structured Data","cat":"text",
            "desc":"AI can read messy text and pull out clean, structured information. Paste any text — a job posting, a news article, an email — and extract key fields as JSON.",
            "hints":["Tell AI exactly what fields to extract","Ask for JSON output","Try with a job description: extract title, salary, skills, location"],
            "task_type":"text","tool":"llm",
            "starter_instruction":"Extract the following fields from the text below and return ONLY valid JSON:\n- company_name\n- job_title\n- salary (if mentioned)\n- required_skills (as array)\n- location\n\nText:",
            "starter_input":"TechCorp Ltd is hiring a Senior Python Developer in Manchester. Salary: £65,000-£80,000. You must know Python, FastAPI, PostgreSQL, and Docker. Remote-friendly with monthly office days."
        },
        {
            "id":6,"title":"Classify & Label","cat":"text",
            "desc":"Sentiment analysis — one of AI's oldest tricks. Classify customer reviews as Positive, Negative, or Neutral. Then build a 5-star rating version.",
            "hints":["Give AI multiple reviews at once","Ask it to classify each with a reason","Try adding a confidence score"],
            "task_type":"text","tool":"llm",
            "starter_instruction":"Classify each review below as Positive, Negative, or Neutral. For each give: label, confidence (high/medium/low), and one-line reason.\n\nReviews:",
            "starter_input":"1. The delivery was fast and the product is exactly as described.\n2. Terrible experience. Broken on arrival and no response from support.\n3. It's okay I suppose. Not amazing but does the job.\n4. Absolutely love it! Worth every penny.\n5. Expected better quality for the price."
        },
        {
            "id":7,"title":"Translate & Localise","cat":"text",
            "desc":"Translate is easy. Localisation is the real skill — adapting content for a culture, not just a language. Ask AI to translate AND explain what it changed culturally.",
            "hints":["Ask for translation + cultural notes","Try British English to American English as a warm-up","Then try English to Hindi or Bengali"],
            "task_type":"text","tool":"llm",
            "starter_instruction":"Translate the following text to Hindi. Then add a 'Cultural Notes' section explaining any phrases you adapted for Indian audiences.\n\nText:",
            "starter_input":"We're over the moon about our new product launch! It's been a real rollercoaster getting here, but we've knocked it out of the park."
        },
        {
            "id":8,"title":"Few-Shot Learning","cat":"text",
            "desc":"Teach AI your style with just 2-3 examples. This is called few-shot prompting. Give examples of input→output, then give a new input — AI follows the pattern.",
            "hints":["Show 2-3 examples in your prompt","Pattern: Input: ... Output: ...","Then write: Input: [your new one] Output:"],
            "task_type":"text","tool":"llm",
            "starter_instruction":"Learn from these examples and follow the same pattern:\n\nInput: The app crashed again\nOutput: 🔴 Bug Report — App stability issue\n\nInput: Users love the new dashboard\nOutput: 🟢 Positive Signal — Dashboard UX\n\nInput: Payment processing is 3x slower this week\nOutput:",
            "starter_input":""
        },
        {
            "id":9,"title":"Chain of Thought","cat":"text",
            "desc":"Make AI think step by step — this dramatically improves accuracy on hard problems. Add 'Think step by step' or 'Show your reasoning' to any prompt.",
            "hints":["Add: 'Think step by step before answering'","Compare with and without this instruction","Works best on maths, logic, and multi-step problems"],
            "task_type":"text","tool":"llm",
            "starter_instruction":"Think step by step before answering.\n\nQuestion: A shop sells apples for £1.20 each. A customer buys 3 apples and pays with a £5 note. The shop gives back one £2 coin and two 20p coins. Is this correct change? If not, what should the correct change be?",
            "starter_input":""
        },
        {
            "id":10,"title":"AI as a Persona","cat":"text",
            "desc":"AI can become anyone — a doctor, a lawyer, a chef, a career coach. Build a System Prompt that defines who AI is, its tone, what it won't say, and its expertise.",
            "hints":["Define: role, tone, expertise, limitations","Try: Career coach for women returning to work","The more specific the persona, the better the output"],
            "task_type":"text","tool":"llm",
            "starter_instruction":"You are Priya, a friendly and direct career coach specialising in helping women re-enter the workforce after a career break. You speak in simple, encouraging language. You never give vague advice — always give specific, actionable steps. You do not discuss topics outside career and professional development.\n\nUser question:",
            "starter_input":"I took 5 years off to raise my kids and I want to get back into marketing. Where do I even start?"
        },

        # ── WEEK 1: Image AI ─────────────────────────────────────────────────
        {
            "id":11,"title":"Your First Image","cat":"image",
            "desc":"Generate your first AI image. Start simple — describe a scene. Then learn the three ingredients of a great image prompt: subject, style, and mood.",
            "hints":["Subject: what is in the image","Style: photorealistic / oil painting / cartoon / watercolour","Mood: warm, dramatic, minimalist, vibrant"],
            "task_type":"image","tool":"imagen",
            "starter_instruction":"A cup of masala chai on a wooden table by a rainy window, photorealistic, warm mood, soft lighting",
            "starter_input":""
        },
        {
            "id":12,"title":"Prompt Crafting for Images","cat":"image",
            "desc":"The same subject, 3 completely different prompts — 3 completely different images. Learn how style, lighting, and artist references change everything.",
            "hints":["Try: 'in the style of...'","Add lighting: golden hour, studio lighting, neon","Add camera: wide angle, close-up, aerial view"],
            "task_type":"image","tool":"imagen",
            "starter_instruction":"A woman reading a book, Studio Ghibli animation style, soft pastel colours, golden afternoon light through a window",
            "starter_input":""
        },
        {
            "id":13,"title":"Generate a Logo","cat":"image",
            "desc":"Create a logo for a real or imaginary business. Learn how to specify shape, colour palette, style (minimalist/vintage/tech), and what to avoid.",
            "hints":["Name the business and what it does","Specify: minimalist / vintage / modern / playful","Add colour: 'using only blue and white'","Say: 'no text, icon only'"],
            "task_type":"image","tool":"imagen",
            "starter_instruction":"A minimalist logo icon for an AI learning app called BlockCode, using purple and white, geometric shapes, modern tech style, no text, clean flat design",
            "starter_input":""
        },
        {
            "id":14,"title":"Product Visualisation","cat":"image",
            "desc":"Businesses use AI to visualise products before they're built. Generate a product mockup — a phone app screen, a packaging design, a room interior.",
            "hints":["Be specific about dimensions and layout","Add: 'product photography style'","Try: 'on a white background, studio lighting'"],
            "task_type":"image","tool":"imagen",
            "starter_instruction":"A smartphone showing a learning app UI with colourful blocks, product photography style, white background, studio lighting, modern flat design",
            "starter_input":""
        },
        {
            "id":15,"title":"Describe an Image (Vision)","cat":"vision",
            "desc":"AI can see. Paste any image URL and ask AI to describe it, extract text from it, identify objects, or analyse what's happening. This is called Computer Vision.",
            "hints":["Give a direct image URL (ends in .jpg or .png)","Ask specific questions about the image","Try: describe, extract text, count objects, identify mood"],
            "task_type":"vision","tool":"vision",
            "starter_instruction":"Describe this image in detail. List: (1) main subject, (2) background, (3) colours, (4) mood, (5) any text visible.",
            "starter_input":"https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PNG_transparency_demonstration_1.png/280px-PNG_transparency_demonstration_1.png"
        },

        # ── WEEK 2: Document AI & RAG ────────────────────────────────────────
        {
            "id":16,"title":"Document Q&A","cat":"rag",
            "desc":"Paste any document — a policy, a contract, a report — and ask questions about it. This is how lawyers, analysts, and researchers use AI to read 100-page documents in minutes.",
            "hints":["Paste the document in Input","Ask a specific question in Instruction","Try: 'What are the key obligations of the buyer?'"],
            "task_type":"rag","tool":"rag",
            "starter_instruction":"Answer the following question based ONLY on the document provided. If the answer is not in the document, say 'Not mentioned in the document.'\n\nQuestion: What does the refund policy say?",
            "starter_input":"TERMS AND CONDITIONS\n\nReturns & Refunds: Customers may return unused items within 30 days of purchase for a full refund. Items must be in original packaging. Digital downloads are non-refundable. Refunds are processed within 5-7 business days.\n\nPrivacy: We collect your name, email, and purchase history. We do not sell your data to third parties. You can request deletion of your data at any time by emailing privacy@example.com.\n\nDelivery: Standard delivery is 3-5 business days. Express delivery (1-2 days) costs an additional £4.99. We deliver to UK addresses only.\n\nWarranty: All products carry a 12-month manufacturer warranty. This does not cover accidental damage."
        },
        {
            "id":17,"title":"Compare Two Documents","cat":"rag",
            "desc":"AI can read two documents side by side and find differences, similarities, or conflicts. Essential for contract review, policy comparison, or research.",
            "hints":["Label documents clearly: DOCUMENT A: ... DOCUMENT B:","Ask for a comparison table","Try: 'What does Document A say that Document B does not?'"],
            "task_type":"text","tool":"llm",
            "starter_instruction":"Compare these two job descriptions and create a table showing: (1) responsibilities in both, (2) responsibilities only in Job A, (3) responsibilities only in Job B, (4) salary difference if any.",
            "starter_input":"JOB A - Marketing Manager at StartupX: Manage social media accounts, create content calendar, run paid ads on Google and Facebook, analyse campaign performance, manage £10k monthly budget. Salary: £45,000.\n\nJOB B - Digital Marketing Lead at CorpY: Lead a team of 3 marketers, oversee all digital channels, manage agency relationships, present quarterly reports to board, manage £50k monthly budget. Salary: £60,000."
        },
        {
            "id":18,"title":"Meeting Notes → Actions","cat":"rag",
            "desc":"Paste messy meeting notes and transform them into: summary, action items with owners, decisions made, and open questions. This saves 30 minutes after every meeting.",
            "hints":["Paste raw notes in Input","Ask for: summary, actions, decisions, open questions","Try adding: 'Format as an email I can send to attendees'"],
            "task_type":"text","tool":"llm",
            "starter_instruction":"From the meeting notes below, extract:\n1. One-paragraph summary\n2. Action items (format: [Owner] - [Task] - [Deadline])\n3. Decisions made\n4. Open questions still unresolved\n\nMeeting notes:",
            "starter_input":"Team sync 15 May. Priya, Raj, Sarah, Tom attended. Missed: Dev team.\n\nDiscussed launch date - Priya wants May 30, Tom thinks too soon, needs more testing. Agreed on June 5 as final date. Tom to finish testing by June 1. \n\nBudget - Sarah said we're 20% over. Need to cut somewhere. Raj suggested cutting the paid ads for the first 2 weeks. No decision yet on this.\n\nApp store listing - Priya to write description by end of this week. Need screenshots, who's doing that? Nobody assigned.\n\nNext meeting: May 22."
        },
        {
            "id":19,"title":"CV Screener","cat":"rag",
            "desc":"Paste a job description and a CV — ask AI to score the match, list gaps, and suggest interview questions. This is real HR AI in use at companies today.",
            "hints":["Put JD first, then CV in Input","Ask for a match score out of 10","Ask for: strengths, gaps, 3 interview questions"],
            "task_type":"text","tool":"llm",
            "starter_instruction":"You are an expert recruiter. Given the Job Description and CV below, provide:\n1. Match score out of 10 with reasoning\n2. Top 3 strengths of this candidate for this role\n3. Top 3 gaps or concerns\n4. 3 specific interview questions to probe the gaps\n\nJOB DESCRIPTION:",
            "starter_input":"JOB: Senior Python Developer. Must have: 5+ years Python, FastAPI or Django, PostgreSQL, AWS, team leadership experience.\n\n---\nCV: Jane Smith. 4 years Python developer at TechCo. Built REST APIs using Flask. Used MySQL. No AWS experience but familiar with Azure. No management experience. BSc Computer Science."
        },
        {
            "id":20,"title":"Email Drafter","cat":"text",
            "desc":"AI writes better emails than most people. Learn to give it context: who you are, who you're writing to, the relationship, the goal, and the tone. Then compare with and without context.",
            "hints":["Give: your role, recipient's role, relationship","State the goal clearly","Specify tone: formal, warm, assertive, apologetic"],
            "task_type":"text","tool":"llm",
            "starter_instruction":"Write a professional but warm email from me (a startup founder) to a potential investor I met briefly at a networking event 2 weeks ago. Goal: ask for a 30-minute intro call to discuss my EdTech startup. Tone: confident but not pushy. Length: under 150 words. Subject line included.",
            "starter_input":""
        },

        # ── WEEK 2: Chatbot & Conversation AI ────────────────────────────────
        {
            "id":21,"title":"Build a Chatbot","cat":"chatbot",
            "desc":"Design a chatbot persona with a clear purpose. Write its system prompt — who it is, what it helps with, its tone, and hard rules (what it will never do). Then test it.",
            "hints":["Define: name, role, tone, expertise","Add rules: 'You will never...'","Test edge cases: what happens if user goes off-topic?"],
            "task_type":"chatbot","tool":"chatbot",
            "starter_instruction":"You are Zara, a friendly customer support agent for an online clothing store called StyleHub. You help with: order tracking, returns, sizing questions, and product availability. You are warm, efficient, and never make promises about refunds without saying 'I'll check that for you.' You do not discuss competitor brands. If you don't know something, say 'Let me look into that for you.'",
            "starter_input":"Hi, I ordered a dress 5 days ago and it hasn't arrived yet."
        },
        {
            "id":22,"title":"Conversation with Memory","cat":"chatbot",
            "desc":"A basic chatbot forgets everything. A useful one remembers context. See how providing conversation history changes the quality of AI responses dramatically.",
            "hints":["The conversation builds up as you chat","Notice how AI refers back to earlier messages","Try contradicting yourself and see if AI notices"],
            "task_type":"chatbot","tool":"chatbot",
            "starter_instruction":"You are a helpful personal assistant. Remember everything the user tells you in this conversation and refer back to it naturally. If the user mentions their name, use it. If they mention a problem, follow up on it.",
            "starter_input":"Hi, I'm Meera. I'm trying to plan a birthday party for my daughter who is turning 7."
        },
        {
            "id":23,"title":"Socratic Tutor","cat":"chatbot",
            "desc":"The best AI tutors don't give answers — they ask questions that lead you to the answer yourself. This is called the Socratic method. Build one.",
            "hints":["System prompt: never give the answer directly","Instead: ask guiding questions","Praise effort, not correctness"],
            "task_type":"chatbot","tool":"chatbot",
            "starter_instruction":"You are a Socratic maths tutor for children aged 8-12. When a student asks for help, NEVER give the answer directly. Instead, ask a guiding question that helps them think. Break problems into small steps. When they get something right, celebrate it. When they're stuck, give a smaller hint. Start by asking what they already know about the problem.",
            "starter_input":"I don't understand fractions. What is 1/2 + 1/4?"
        },

        # ── WEEK 3: Code AI ──────────────────────────────────────────────────
        {
            "id":24,"title":"Code from Description","cat":"code",
            "desc":"Describe what you want in plain English — AI writes the code. This is how non-developers use AI to automate their work. You don't need to know how to code to get useful code.",
            "hints":["Be specific: language, inputs, outputs, edge cases","Say: 'Add comments explaining each step'","Ask for an example of how to run it"],
            "task_type":"text","tool":"llm",
            "starter_instruction":"Write a Python function that takes a list of student names and scores (as a dictionary), and returns: (1) the top 3 students, (2) the class average, (3) how many students are above average. Add comments. Show an example of how to call it.",
            "starter_input":""
        },
        {
            "id":25,"title":"Debug with AI","cat":"code",
            "desc":"Paste broken code and ask AI to find the bug, explain what's wrong, and give the fixed version. This is one of the highest-ROI uses of AI for developers.",
            "hints":["Paste the broken code in Input","Describe what it should do","Ask: explain the bug, then show the fix"],
            "task_type":"text","tool":"llm",
            "starter_instruction":"The code below has a bug. (1) Identify exactly what the bug is and why it happens, (2) explain what the code is trying to do, (3) provide the corrected version.\n\nCode:",
            "starter_input":"def calculate_average(numbers):\n    total = 0\n    for num in numbers:\n        total = total + num\n    average = total / len(numbers)\n    return average\n\nresult = calculate_average([])\nprint(result)"
        },
        {
            "id":26,"title":"Explain Any Code","cat":"code",
            "desc":"Paste any code and get a plain-English explanation. Understand what a function does, why a library is used, or what a complex algorithm is doing — without being a developer.",
            "hints":["Paste the code in Input","Ask for: overall purpose, line-by-line explanation, potential issues","Try with code from your own projects"],
            "task_type":"text","tool":"llm",
            "starter_instruction":"Explain the following code to someone who has never programmed before. Cover: (1) what the code does overall, (2) explain each section in plain English, (3) what would happen if we changed the input.\n\nCode:",
            "starter_input":"import re\n\ndef extract_emails(text):\n    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}'\n    return re.findall(pattern, text)\n\ntext = 'Contact us at hello@company.com or support@help.org for assistance.'\nemails = extract_emails(text)\nprint(f'Found {len(emails)} emails: {emails}')"
        },

        # ── WEEK 3: Advanced AI ──────────────────────────────────────────────
        {
            "id":27,"title":"AI Self-Critique","cat":"advanced",
            "desc":"Ask AI to generate something, then ask it to critique its own output and improve it. This two-step process (generate → critique → improve) produces dramatically better results.",
            "hints":["Step 1: generate the content","Step 2: ask AI to critique it harshly","Step 3: ask AI to rewrite based on the critique"],
            "task_type":"text","tool":"llm",
            "starter_instruction":"STEP 1: Write a 3-sentence pitch for an AI learning app for parents.\n\nSTEP 2: Critique that pitch — what's weak, vague, or unconvincing?\n\nSTEP 3: Rewrite the pitch addressing every criticism. Label each step clearly.",
            "starter_input":""
        },
        {
            "id":28,"title":"Multi-Step Reasoning","cat":"advanced",
            "desc":"Complex problems require multiple reasoning steps. Learn to break a big problem into a chain of AI calls — each output feeds the next input. This is the foundation of AI agents.",
            "hints":["Step 1: analyse the problem","Step 2: generate options","Step 3: evaluate each option","Step 4: make a recommendation"],
            "task_type":"text","tool":"llm",
            "starter_instruction":"Use multi-step reasoning to solve this business problem. Work through it in 4 clearly labelled steps:\nStep 1 - Understand the problem and identify key constraints\nStep 2 - Generate 3 possible solutions\nStep 3 - Evaluate each solution on cost, speed, and risk\nStep 4 - Recommend the best solution with justification\n\nProblem:",
            "starter_input":"A small bakery is losing customers to a new competitor. They have £2,000 to invest, one month to act, and a team of 3 people. Their strengths are quality products and loyal existing customers. Their weakness is zero online presence."
        },
        {
            "id":29,"title":"Build a Content Pipeline","cat":"advanced",
            "desc":"One idea → blog post → social posts → email newsletter → image prompt. This is how content teams use AI to multiply one piece of content into many. Build the full pipeline.",
            "hints":["Give one core idea or topic","Ask AI to produce all formats in one prompt","Use clear section headers for each format"],
            "task_type":"text","tool":"llm",
            "starter_instruction":"From the single idea below, create a full content package:\n1. Blog post title and 300-word post\n2. 3 LinkedIn posts (short, punchy, one insight each)\n3. 1 Twitter/X thread (5 tweets)\n4. Email newsletter (subject line + 150 words)\n5. Image generation prompt for a hero image\n\nIdea:",
            "starter_input":"AI is changing how parents help their children with homework — for better and for worse."
        },
        {
            "id":30,"title":"Your AI Product Idea","cat":"advanced",
            "desc":"You've learned prompting, image generation, vision, RAG, chatbots, code AI, and advanced techniques. Now: design YOUR AI product. What problem does it solve? Who is it for? How would it work?",
            "hints":["Think about a problem in your own life","Which AI techniques from this course would it use?","Ask AI to help you refine and stress-test your idea"],
            "task_type":"text","tool":"llm",
            "starter_instruction":"You are a product strategist and AI expert. Help me develop my AI product idea by providing:\n1. Refined problem statement (who has this problem, how painful is it)\n2. AI solution architecture (which AI capabilities would power it)\n3. MVP feature list (the 3 most important features to build first)\n4. Biggest risks and how to mitigate them\n5. A one-paragraph pitch I could say to an investor in 60 seconds\n\nMy rough idea:",
            "starter_input":"I want to build an app that helps parents teach their kids about money and savings using AI."
        },
    ]
}


def get_task(role, level_idx):
    idx = level_idx - 1
    if role not in TASKS or idx < 0 or idx >= len(TASKS[role]):
        return None
    return TASKS[role][idx]

def get_max_level(role):
    return len(TASKS.get(role, []))
