# server/app.py

import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
from dotenv import load_dotenv
import requests
# ---- Load environment variables ----
load_dotenv()
openai.api_key = os.getenv("GROQ_API_KEY")
openai.api_base = "https://api.groq.com/openai/v1"

# ---- Flask App Setup ----
app = Flask(__name__)
CORS(app)

# ---- Keyword → Career Mapping ----
career_mapping = {
    "drawing": ["Graphic Designer", "Illustrator", "Animator"],
    "coding": ["Software Engineer", "AI Developer", "Backend Developer"],
    "speaking": ["Motivational Speaker", "Sales Manager", "Lawyer"],
    "sports": ["Athlete", "Fitness Coach", "Sports Analyst"],
    "writing": ["Content Writer", "Editor", "Author"],
    "math": ["Data Scientist", "Statistician", "Finance Analyst"],
    "science": ["Researcher", "Biotech Engineer", "Pharmacist"],
    "music": ["Musician", "Sound Engineer", "Music Producer"],
    "cooking": ["Chef", "Food Blogger", "Nutritionist"],
    "travel": ["Travel Blogger", "Tour Guide", "Flight Attendant"],
    "technology": ["Cybersecurity Analyst", "IT Consultant", "DevOps Engineer"],
    "design": ["UI/UX Designer", "Interior Designer", "Fashion Designer"],
    "marketing": ["Digital Marketer", "SEO Analyst", "Brand Manager"],
    "finance": ["Investment Banker", "Accountant", "Financial Analyst"],
    "helping": ["Social Worker", "Psychologist", "Therapist"],
    "language": ["Translator", "Linguist", "Interpreter"],
    "leadership": ["Project Manager", "Team Lead", "Business Owner"],
}

# ---- Prompt Generator ----
def generate_prompt(user_input):
    matched_careers = []

    for keyword, careers in career_mapping.items():
        if keyword.lower() in user_input.lower():
            matched_careers.extend(careers)

    career_list = ", ".join(set(matched_careers)) if matched_careers else "any relevant careers based on the user's input"

    return f"""
You are an empathetic AI career coach. The user shared this interest: "{user_input}".

Based on that, suggest **exactly 3 exciting career paths** from: {career_list}. For each:

1. **Career Overview** (1–2 lines)
2. **Why it aligns** (match to interest or trait)
3. **Skills Needed**:
   - Technical
   - Soft
4. **One Online Course** (name + platform + link)
5. **One YouTube Channel** (short name only)
6. **Mini Project Idea** (simple)
7. **Top Companies Hiring** (just 2–3)
8. **Future Outlook** (1–2 lines)

🎯 Format clearly with bold headers and bullets. Be short, visually clean, and inspiring.
"""


    if matched_careers:
        career_list = ", ".join(set(matched_careers))
        base_instruction += f"\nThese match to potential roles like: {career_list}.\nPick the most exciting 3 from these and continue."

    return base_instruction


# ---- Groq API Call ----
def ask_gpt(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {os.getenv("GROQ_API_KEY")}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",  # ✅ Use valid Groq model
        "messages": [
            {"role": "system", "content": "You are a helpful AI career counselor."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 500
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()

# ---- API Endpoint ----
@app.route("/get-career", methods=["POST"])
def get_career():
    data = request.json
    message = data.get("message", "")

    if not message:
        return jsonify({"reply": "Please describe your interests or skills."}), 400

    prompt = generate_prompt(message)
    reply = ask_gpt(prompt)

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
