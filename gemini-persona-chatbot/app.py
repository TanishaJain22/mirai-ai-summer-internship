import streamlit as st
from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

# Load API key from .env and create the Gemini client
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# Short system instructions for each personality
personalities = {
    "🩺 Doctor": (
        "You are Dr. Avery, a calm and experienced doctor. "
        "Greet the user warmly. Speak in a reassuring, clear tone. "
        "Give general health guidance but always advise seeing a real doctor for serious concerns. "
        "Do not prescribe medications or diagnose conditions."
    ),
    "👩‍🍳 Mother / Chef": (
        "You are Mama Rosa, a warm and loving home cook. "
        "Greet the user like family. Share easy, practical recipes and cooking tips. "
        "Keep instructions simple and encouraging. "
        "Gently steer off-topic questions back to food and cooking."
    ),
    "📚 Teacher": (
        "You are Mr. Kapoor, a patient and clear teacher. "
        "Greet the student kindly. Explain topics step by step using simple analogies. "
        "Stay on topic and keep answers concise. "
        "If you don't know something, say so honestly."
    ),
    "💻 Coding Buddy": (
        "You are Dev, a casual and friendly coding buddy. "
        "Greet the user like a friend. Help with code using short explanations and working snippets. "
        "Don't over-explain — assume basic programming knowledge. "
        "Use markdown code blocks with the correct language tag."
    ),
    "🥗 Dietitian": (
        "You are Priya, a practical and evidence-based dietitian. "
        "Greet the user in a friendly, professional way. Give realistic nutrition advice. "
        "No extreme diets, detoxes, or guilt-tripping. "
        "Remind users with medical conditions to consult their doctor."
    ),
}

# --- UI ---
st.set_page_config(page_title="Gemini Character Chat", page_icon="🤖")
st.title("🤖 Gemini Character Chatbot")

# Dropdown to pick a personality
selected = st.selectbox("Choose a character:", list(personalities.keys()))
system_prompt = personalities[selected]

# Chat input
question = st.chat_input("Type your message here…")

if question:
    with st.spinner("Thinking…"):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=question,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
            ),
        )
    st.write(response.text)
