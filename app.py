import os
from flask import Flask, request, jsonify, send_from_directory
from openai import OpenAI

app = Flask(__name__, static_folder="static")
MODEL = os.getenv("OPENAI_MODEL", "gpt-5.5")

@app.get("/")
def home():
    return send_from_directory("static", "index.html")

@app.post("/api/teach")
def teach():
    if not os.getenv("OPENAI_API_KEY"):
        return jsonify(error="সার্ভারে OPENAI_API_KEY সেট করা হয়নি।"), 503
    data = request.get_json(silent=True) or {}
    code = str(data.get("code", ""))[:12000]
    error = str(data.get("error", ""))[:6000]
    question = str(data.get("question", ""))[:3000]
    if not code.strip() and not question.strip():
        return jsonify(error="কোড বা প্রশ্ন লিখুন।"), 400

    prompt = f"""শিক্ষার্থীর কোড:
```python
{code}
```

চালানোর সময় পাওয়া error/traceback:
{error or "কোনো runtime error দেওয়া হয়নি।"}

শিক্ষার্থীর প্রশ্ন:
{question or "কোডটি পরীক্ষা করে ভুল থাকলে ব্যাখ্যা করুন।"}

কাজ:
১) কোডে নিশ্চিত ভুল, সম্ভাব্য ভুল এবং শুধু style/উন্নতির পরামর্শ আলাদা করুন।
২) error থাকলে কোন লাইনে/কোন কারণে হয়েছে ব্যাখ্যা করুন। traceback না থাকলে বানিয়ে বলবেন না।
৩) সংশোধিত সম্পূর্ণ কোড দিন।
৪) প্রতিটি পরিবর্তন সহজ, পরিষ্কার বাংলায় বুঝিয়ে দিন; Python keyword ইংরেজিতেই রাখুন।
৫) কোডের উদ্দেশ্য অস্পষ্ট হলে অনুমান না করে প্রশ্ন করুন।
৬) কোড নিরাপদ কি না সংক্ষেপে বলুন। অজানা কোড execute হয়েছে বলে দাবি করবেন না।
৭) একেবারে নতুন শিক্ষার্থীকে শিক্ষকসুলভ, ধাপে ধাপে বোঝান।
"""
    try:
        client = OpenAI()
        response = client.responses.create(
            model=MODEL,
            instructions="তুমি একজন নির্ভুল, ধৈর্যশীল Python শিক্ষক। বাংলায় উত্তর দাও। ভুল বানিয়ে বলবে না; uncertainty স্পষ্ট করো।",
            input=prompt,
            max_output_tokens=1800,
        )
        return jsonify(answer=response.output_text)
    except Exception as exc:
        app.logger.exception("AI request failed")
        return jsonify(error=f"AI request ব্যর্থ হয়েছে: {type(exc).__name__}: {exc}"), 502

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
