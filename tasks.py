# tasks.py
TASKS = {
    "kid": [
        {"id":1, "title":"Hello Print", "desc":"Print 'Hello, AI!' to screen", "hints":["Use print()","Wrap text in quotes","Check spelling"], "success_keys":["print","hello"], "cat":"coding"},
        {"id":2, "title":"Asterisk Line", "desc":"Print ***** using string multiplication", "hints":["Use '*'","Multiply by 5","Print result"], "success_keys":["print","*","5"], "cat":"coding"},
        {"id":3, "title":"Number Counter", "desc":"Print 1 to 5 using a loop", "hints":["Use for loop","range(1,6)","print(i)"], "success_keys":["for","range","print"], "cat":"coding"},
        {"id":4, "title":"Asterisk Triangle", "desc":"Print right triangle of * height 4", "hints":["Loop 1-4","'*' * i inside loop","print each line"], "success_keys":["for","range","*","print"], "cat":"coding"},
        {"id":5, "title":"Sum Two Numbers", "desc":"Add 12 + 34 and print", "hints":["Use + operator","Store in variable","print result"], "success_keys":["+","print","="], "cat":"math"},
        {"id":6, "title":"Even/Odd Checker", "desc":"Check if 7 is even or odd", "hints":["Use % operator","if num%2==0","else print odd"], "success_keys":["%","if","else","print"], "cat":"math"},
        {"id":7, "title":"Leap Year Logic", "desc":"Check if 2024 is leap year", "hints":["divisible by 4","not by 100 unless by 400","if/elif chain"], "success_keys":["if","%","and","or"], "cat":"science"},
        {"id":8, "title":"Count Vowels", "desc":"Count vowels in 'education'", "hints":["loop through string","check in 'aeiou'","counter+=1"], "success_keys":["for","in","if","counter"], "cat":"english"},
        {"id":9, "title":"Reverse Word", "desc":"Reverse 'python' using slicing", "hints":["use [::-1]","store in var","print it"], "success_keys":["[::-1]","print"], "cat":"coding"},
        {"id":10, "title":"Average Calculator", "desc":"Find avg of 10,20,30", "hints":["sum them","divide by 3","use ()"], "success_keys":["+","/","print"], "cat":"math"},
        {"id":11, "title":"FizzBuzz Lite", "desc":"Print 1-10, replace 3 with Fizz, 5 with Buzz", "hints":["loop 1-10","if i%3==0","elif i%5==0"], "success_keys":["for","if","%","print"], "cat":"coding"},
        {"id":12, "title":"Max in List", "desc":"Find max in [4,9,2,7]", "hints":["use max()","or loop compare","track highest"], "success_keys":["max","or","for","if"], "cat":"math"},
        {"id":13, "title":"Word Count", "desc":"Count words in 'I love AI coding'", "hints":["split string","len()","print count"], "success_keys":["split","len","print"], "cat":"english"},
        {"id":14, "title":"Case Swap", "desc":"Convert 'Hello' to 'hELLO'", "hints":["swapcase()","or loop char by char","print"], "success_keys":["swapcase","or","print"], "cat":"english"},
        {"id":15, "title":"Factorial", "desc":"Calculate 5! (120)", "hints":["start result=1","loop 1-5","result*=i"], "success_keys":["for","*=","print"], "cat":"math"},
        {"id":16, "title":"Palindrome Check", "desc":"Check if 'racecar' reads same backwards", "hints":["reverse string","compare ==","if/else"], "success_keys":["[::-1]","==","if"], "cat":"coding"},
        {"id":17, "title":"Grade Calculator", "desc":"Print A/B/C/D based on score >=90/80/70/60", "hints":["if/elif chain","score>=90","print letter"], "success_keys":["if","elif","print"], "cat":"math"},
        {"id":18, "title":"Sum Digits", "desc":"Sum digits of 1234", "hints":["convert to str","loop chars","int(char) add"], "success_keys":["for","int","+","sum"], "cat":"math"},
        {"id":19, "title":"Prime Check", "desc":"Check if 17 is prime", "hints":["loop 2 to num-1","if num%i==0 return False","else True"], "success_keys":["for","%","if","return"], "cat":"math"},
        {"id":20, "title":"List Filter", "desc":"Keep only numbers >5 from [2,7,1,9,3]", "hints":["new list=[]","for n in list","if n>5 append"], "success_keys":["for","if","append"], "cat":"coding"},
        {"id":21, "title":"Temperature Convert", "desc":"Convert 32°C to °F (formula: *9/5+32)", "hints":["multiply 9/5","add 32","print result"], "success_keys":["*","/","+","print"], "cat":"science"},
        {"id":22, "title":"Fibonacci Lite", "desc":"Print first 6 Fibonacci numbers", "hints":["a=0,b=1","loop 6 times","print a, a,b=b,a+b"], "success_keys":["for","a,b","print"], "cat":"math"},
        {"id":23, "title":"String Replace", "desc":"Replace 'cat' with 'dog' in string", "hints":["use .replace()","print new string"], "success_keys":["replace","print"], "cat":"english"},
        {"id":24, "title":"Guess Number Logic", "desc":"Simulate: if guess==7 print win, else try again", "hints":["if guess==7","print win","else print try"], "success_keys":["if","==","print","else"], "cat":"coding"},
        {"id":25, "title":"Matrix Row Sum", "desc":"Sum first row of [[1,2],[3,4]]", "hints":["row[0]","sum()","print"], "success_keys":["sum","print"], "cat":"math"},
        {"id":26, "title":"Alphabet Order", "desc":"Check if letters in 'ace' are ascending", "hints":["list()","== sorted()","if/else"], "success_keys":["sorted","==","if"], "cat":"english"},
        {"id":27, "title":"Gravity Calc", "desc":"Calculate distance: 0.5*9.8*t^2 for t=3", "hints":["use ** for power","0.5*9.8*t**2","print"], "success_keys":["*","**","print"], "cat":"science"},
        {"id":28, "title":"Frequency Counter", "desc":"Count 'a' in 'banana'", "hints":[".count()","or loop","print"], "success_keys":["count","or","for","print"], "cat":"english"},
        {"id":29, "title":"Tic-Tac-Toe Grid", "desc":"Print 3x3 grid using nested loops", "hints":["for i in range(3)","for j in range(3)","print end=''"], "success_keys":["for","range","print"], "cat":"coding"},
        {"id":30, "title":"Story Generator", "desc":"Combine name, place, action into sentence", "hints":["f-strings","f'{name} went to {place}'","print"], "success_keys":["f'","print"], "cat":"english"}
    ],
    "adult": [
        {"id":1, "title":"LLM Fetch Block", "desc":"Create block to call Gemini API with prompt", "hints":["Add model dropdown","set temperature","pass prompt input"], "success_keys":["model","temperature","prompt"], "cat":"ai"},
        {"id":2, "title":"Context Injection", "desc":"Add system prompt block before LLM", "hints":["use context block","prepend to prompt","set role"], "success_keys":["context","system","prepend"], "cat":"ai"},
        {"id":3, "title":"JSON Output Parser", "desc":"Parse LLM response into dict", "hints":["json.loads()","try/except","handle errors"], "success_keys":["json","loads","try"], "cat":"data"},
        {"id":4, "title":"Retry Logic", "desc":"Retry LLM call up to 3 times on failure", "hints":["for range(3)","try/except","break on success"], "success_keys":["for","try","except","break"], "cat":"ai"},
        {"id":5, "title":"Fallback Model", "desc":"If primary fails, switch to backup model", "hints":["if error","change model var","re-run"], "success_keys":["if","error","switch"], "cat":"ai"},
        {"id":6, "title":"Text Summarizer", "desc":"Summarize long text to 3 bullets", "hints":["prompt: 'Summarize in 3 bullets'","parse output","format list"], "success_keys":["summarize","bullets","format"], "cat":"ai"},
        {"id":7, "title":"Sentiment Analyzer", "desc":"Classify text as positive/negative/neutral", "hints":["prompt with labels","parse result","return dict"], "success_keys":["classify","labels","parse"], "cat":"ai"},
        {"id":8, "title":"Translation Pipeline", "desc":"Translate EN to FR using LLM", "hints":["prompt: 'Translate to French'","pass text","capture output"], "success_keys":["translate","French","prompt"], "cat":"ai"},
        {"id":9, "title":"RAG Chunker", "desc":"Split text into 200-char chunks with overlap", "hints":["range step size","slice text","store list"], "success_keys":["slice","range","overlap"], "cat":"data"},
        {"id":10, "title":"Vector Embed Sim", "desc":"Convert chunks to mock embeddings", "hints":["hash text","normalize","list of floats"], "success_keys":["hash","normalize","list"], "cat":"data"},
        {"id":11, "title":"Semantic Search", "desc":"Find closest chunk to query using cosine sim", "hints":["dot product","normalize","max index"], "success_keys":["dot","cosine","max"], "cat":"data"},
        {"id":12, "title":"Prompt Template", "desc":"Create reusable prompt with variables", "hints":[".format() or f-string","{user_input}","store template"], "success_keys":["template","format","var"], "cat":"ai"},
        {"id":13, "title":"Memory Block", "desc":"Store last 5 conversations for context", "hints":["deque(maxlen=5)","append","join for context"], "success_keys":["deque","append","context"], "cat":"ai"},
        {"id":14, "title":"Tool Caller", "desc":"Call calculator/weather API based on query", "hints":["if 'calc' in query","return math","else default"], "success_keys":["if","call","return"], "cat":"ai"},
        {"id":15, "title":"Output Validator", "desc":"Check if LLM output matches schema", "hints":["required keys","all(k in d)","raise if missing"], "success_keys":["keys","all","validate"], "cat":"data"},
        {"id":16, "title":"Rate Limiter", "desc":"Delay calls if >5 req/min", "hints":["track timestamps","time.time()","if len>5 sleep"], "success_keys":["time","sleep","track"], "cat":"infra"},
        {"id":17, "title":"Multi-Agent Router", "desc":"Route query to math/coding/writer agent", "hints":["classify intent","map to agent","dispatch"], "success_keys":["classify","map","route"], "cat":"ai"},
        {"id":18, "title":"Feedback Loop", "desc":"Ask user if output was good, adjust prompt", "hints":["prompt: 'Rate 1-5'","if <3 refine","re-run"], "success_keys":["rate","refine","loop"], "cat":"ai"},
        {"id":19, "title":"Cost Tracker", "desc":"Estimate token cost per call", "hints":["count chars/4","multiply rate","log total"], "success_keys":["tokens","rate","log"], "cat":"infra"},
        {"id":20, "title":"Deployment Flow", "desc":"Package pipeline into CLI/web endpoint", "hints":["Flask route","load pipeline","return json"], "success_keys":["route","return","json"], "cat":"infra"}
    ]
}

def get_task(role, level_idx):
    idx = level_idx - 1
    if role not in TASKS or idx < 0 or idx >= len(TASKS[role]):
        return None
    return TASKS[role][idx]

def get_max_level(role):
    return len(TASKS.get(role, []))