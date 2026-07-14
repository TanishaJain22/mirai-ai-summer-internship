# The Memory Vault — Stateful Chatbot

A Streamlit chatbot powered by Google's Gemini API that **remembers your entire conversation** using `st.session_state`. Choose from 5 personas — Doctor, Teacher, Coding Buddy, Mother/Chef, and Dietitian — and chat without losing context.

---

## What Changed from the Previous Version

This project builds on [`gemini-persona-chatbot`](../gemini-persona-chatbot). Here's what's different:

| Before (v1) | After — Memory Vault (v2) |
|---|---|
| Every message was forgotten on rerun — Streamlit re-runs the script top-to-bottom on each interaction, wiping all local variables | Conversation history is stored in `st.session_state.messages`, a special dict that **survives reruns** |
| Used `st.text_input` + a button for input | Uses `st.chat_input()` for a native chat bar pinned to the bottom of the page |
| No chat replay — old messages disappeared | A `for` loop replays every saved message on each rerun so the full conversation stays visible |
| Single-turn interaction only | Multi-turn memory — the user can scroll back through the entire session |

### Key Concepts Used

- **`st.session_state`** — a persistent dictionary that keeps data alive across Streamlit reruns
- **Chat history replay loop** — iterates over saved messages and re-renders them with `st.chat_message()`
- **Walrus operator (`:=`)** — assigns the chat input and checks it in a single line

---

## How to Run

1. **Clone the repo** and navigate to this folder:
   ```bash
   cd memory-vault-chatbot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file** in this folder with your Gemini API key (see `.env.example`):
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
