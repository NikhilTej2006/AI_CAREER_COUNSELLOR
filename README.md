# 🚀 Career Compass AI – Intelligent Career Path Recommendation Chatbot

> Empowering users to discover their dream careers using the power of AI and immersive design.

---

## 🧠 Overview

**Career Compass AI** is an intelligent chatbot designed to recommend personalized career paths based on user interests like AI, gaming, finance, and more. Using a combination of keyword detection and GPT-driven fallback prompts, the system generates structured, inspiring, and informative responses. It features a beautifully designed, futuristic chat interface reminiscent of platforms like ChatGPT or Gemini.

---

## 🌟 Features

- 🤖 AI-powered career suggestions with context awareness
- 💬 Fully responsive full-screen chat UI
- ✨ Animated typing indicators and avatars
- 🔗 Clickable course & resource links
- 🎯 Career details include skills, projects, courses, companies, and future scope
- 🎨 Clean, futuristic visual design with dynamic backgrounds

---

## 🛠 Tech Stack

### 🔹 Frontend
- **React.js** – Interactive user interface
- **CSS3** – Modern styling, animations, and layout
- **Axios** – Client-server communication

### 🔹 Backend
- **Python + Flask** – REST API for chat requests
- **OpenAI GPT** – For generating detailed career suggestions
- **Prompt Engineering** – For structured response generation

---

## 📁 Folder Structure
career-compass-ai/
├── backend/
│ ├── app.py # Flask server & prompt logic
│ └── requirements.txt # Python dependencies
├── frontend/
│ ├── public/
│ ├── src/
│ │ ├── components/
│ │ │ └── ChatBox.jsx # Chat component
│ │ ├── App.jsx
│ │ ├── App.css
│ │ └── index.js
├── README.md
├── package.json
└── .gitignore

---

## 🧪 How It Works

1. **User Input** – User enters interests (e.g., "I love gaming and coding").
2. **Keyword Match** – Backend checks for mapped career paths.
3. **Prompt Generation** – If matched, a specific GPT prompt is constructed.
4. **Fallback** – If unmatched, a broader exploratory GPT prompt is used.
5. **AI Response** – GPT returns structured text including:
   - Career overview
   - Required skills
   - Top courses with links
   - YouTube resources
   - Projects
   - Hiring companies
   - Career outlook
   - Motivational quote
6. **Render** – Response is shown in chat bubbles with avatars and formatted text.

---

## 🚀 Getting Started

### 🔧 Prerequisites
- Node.js & npm
- Python 3.7+
- OpenAI API Key

### ⚙ Backend Setup
```bash
cd backend
pip install -r requirements.txt
python app.py
cd frontend
npm install
npm start
