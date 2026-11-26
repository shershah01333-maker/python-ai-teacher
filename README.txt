Python AI শিক্ষক — সেটআপ নির্দেশিকা (বাংলা)
==========================================

এই ফোল্ডারে আছে:
- static/index.html : ওয়েবসাইট
- app.py            : AI শিক্ষকের backend
- requirements.txt  : প্রয়োজনীয় Python package
- .env.example      : API key রাখার নমুনা

গুরুত্বপূর্ণ:
* Python code চালানো ও traceback দেখা ওয়েবসাইটের Run Code সুবিধা দিয়ে হয়।
* AI শিক্ষক কোড, error ও আপনার প্রশ্ন বিশ্লেষণ করে বাংলায় ব্যাখ্যা এবং সংশোধিত কোড দিতে পারে।
* কোনো AI-ই সব ধরনের bug ১০০% ধরতে পারে না। বিশেষ করে business logic, environment, dependency, network, concurrency বা অজানা input-এর সমস্যা আলাদা পরীক্ষা চাইতে পারে।
* OpenAI API ব্যবহারে API key এবং API usage-এর খরচ হতে পারে। ChatGPT subscription এবং API billing আলাদা।
* API key কখনো index.html বা public GitHub-এ লিখবেন না। এটি শুধু server-এর environment variable/.env ফাইলে রাখবেন।

কম্পিউটারে চালানোর ধাপ (Windows):
1. Python 3.10 বা নতুন সংস্করণ ইনস্টল করুন।
2. এই folder-এ Terminal / Command Prompt খুলুন।
3. লিখুন:
   py -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
4. .env.example ফাইল কপি করে .env নামে রাখুন।
5. .env ফাইলে আপনার API key দিন:
   OPENAI_API_KEY=আপনার_API_KEY
   OPENAI_MODEL=gpt-5.5
6. সার্ভার চালান:
   python app.py
7. Chrome-এ খুলুন:
   http://127.0.0.1:5000

Linux / macOS:
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   cp .env.example .env
   # .env ফাইলে API key বসান
   python app.py
তারপর http://127.0.0.1:5000 খুলুন।

মোবাইলে:
এই project-টি সরাসরি HTML ফাইল খুললে কোডের Run সুবিধা চলতে পারে, কিন্তু AI শিক্ষক কাজ করবে না।
AI চালাতে backend server অনলাইনে deploy করতে হবে। এটি শুধু ফোনে ফাইল খুলে চালু করা যায় না।
সার্ভার deploy করার সময় OPENAI_API_KEY-কে hosting provider-এর Secret/Environment Variables-এ রাখুন।
সবার জন্য public করলে login, rate limit, abuse protection এবং খরচের সীমা যোগ করুন।

নিরাপত্তা:
- এই editor-এ অপরিচিত বা ক্ষতিকর code চালাবেন না।
- Pyodide browser-এর ভেতরে Python চালায়; browser sandbox থাকলেও এটিকে নিরাপত্তার নিশ্চয়তা ভাববেন না।
- AI-কে পাঠানোর আগে password, API key, ব্যক্তিগত বা গোপন তথ্য মুছে দিন।
- AI-র দেওয়া code নিজে পড়ে বুঝে তারপর চালান।

AI backend OpenAI-এর Responses API ব্যবহার করে।
API documentation: https://developers.openai.com/api/docs/quickstart
