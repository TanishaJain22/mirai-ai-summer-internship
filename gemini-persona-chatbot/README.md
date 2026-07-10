# Gemini Persona Chatbot

A Streamlit chatbot powered by Google's Gemini API that responds in different personas — **Doctor, Teacher, Coding Buddy, Mother/Chef, and Dietitian** — each with a unique personality, tone, and expertise area.

---

## Features

- **5 distinct personas** — pick one from a dropdown and chat instantly
- **Gemini 2.5 Flash** under the hood for fast, high-quality responses
- Each persona has a tailored system prompt that shapes its behaviour
- Clean, single-page Streamlit UI

---

## How to Run

1. **Clone the repo** and navigate to this folder:
   ```bash
   cd gemini-persona-chatbot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file** in this folder with your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

4. **Start the app:**
   ```bash
   streamlit run app.py
   ```

---

## Tech Stack

- Python
- Streamlit
- Google Gemini API (`google-genai`)
- python-dotenv
