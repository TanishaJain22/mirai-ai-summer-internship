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

# ───────────────────────────────────────────────────────────────────
# STEP 1 — Create a "memory box" (runs once, then is skipped)
# ───────────────────────────────────────────────────────────────────
# WHY: Streamlit re-runs the entire script from top to bottom every
#      time the user interacts with anything (click, type, select).
#      Normal variables are destroyed on each rerun.
#
#      st.session_state is a special dictionary that SURVIVES reruns.
#      Think of it like a shelf in a cupboard — you put things on it,
#      and they stay there even when you leave the room and come back.
#
# HOW: We check "is there already a shelf called 'messages'?"
#      If not, we create one (an empty list).
#      If it already exists (from a previous rerun), we skip this
#      so we don't accidentally erase saved messages.
# ───────────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

# ───────────────────────────────────────────────────────────────────
# STEP 2 — Redraw every old message on screen
# ───────────────────────────────────────────────────────────────────
# WHY: Because the script re-runs from scratch, the visible chat
#      bubbles disappear too. We need to loop through our saved list
#      and paint each one back onto the screen.
#
# HOW: Each saved message is a dict like:
#        {"role": "user",      "content": "Hi there"}
#        {"role": "assistant", "content": "Hello! How can I help?"}
#      st.chat_message(role) creates a chat bubble with the right
#      icon (person for "user", robot for "assistant").
# ───────────────────────────────────────────────────────────────────
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ───────────────────────────────────────────────────────────────────
# STEP 3 — Chat input using the walrus operator (:=)
# ───────────────────────────────────────────────────────────────────
# WHY: st.chat_input() gives us the nice built-in chat bar at the
#      bottom of the page (no need for a separate text box + button).
#
# HOW: The walrus operator (:=) does TWO things in one line:
#        1. Assigns whatever the user typed to `user_message`
#        2. Checks if it's truthy (not None / not empty)
#      So this single line says: "grab the input AND, if there
#      actually is one, run the code inside."
# ───────────────────────────────────────────────────────────────────
if user_message := st.chat_input("Say something:"):

    # ───────────────────────────────────────────────────────────────
    # STEP 4a — Save the user's message into our memory box
    # ───────────────────────────────────────────────────────────────
    # We append it BEFORE displaying so it's already stored if the
    # page reruns unexpectedly.
    st.session_state.messages.append({"role": "user", "content": user_message})

    # Display the user's message bubble on screen right now
    with st.chat_message("user"):
        st.markdown(user_message)

    # ───────────────────────────────────────────────────────────────
    # Call Gemini to get the AI's reply
    # ───────────────────────────────────────────────────────────────
    with st.chat_message("assistant"):
        with st.spinner("Thinking…"):
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=user_message,
                config=types.GenerateContentConfig(
                    system_instruction=system_prompt,
                ),
            )
        st.markdown(response.text)

    # ───────────────────────────────────────────────────────────────
    # STEP 4b — Save the assistant's reply into our memory box
    # ───────────────────────────────────────────────────────────────
    st.session_state.messages.append({"role": "assistant", "content": response.text})
