# 📖 StoryVerse — AI-Powered Visual Novel

A Streamlit interactive visual novel powered by Google's Gemini API that generates branching stories, AI artwork, and text-to-speech narration in real time. Choose a genre and art style, then shape the adventure through your decisions.

## ✨ Features

- 📚 **8 story genres** — Dark Fantasy, Cyberpunk Thriller, Post-Apocalyptic Survival, Psychological Horror, Space Opera, Mythological Adventure, Detective Mystery, and Time Travel
- 🎨 **8 art styles** — Anime, Cinematic Realism, Studio Ghibli, Comic Book, Pixel Art, Dark Gothic, Fantasy Concept Art, and Oil Painting
- 🖼️ **AI-generated illustrations** for every scene via Pollinations AI
- 🔊 **Text-to-speech narration** using Microsoft Edge TTS
- 🔀 **Branching choices** — three unique options at the end of each scene that meaningfully alter the story
- 🧠 **Persistent story memory** — Gemini maintains context across scenes so characters, setting, and mysteries stay consistent
- 🛡️ **Graceful error handling** — story, image, and audio failures are caught independently so the experience continues

## 🚀 How to Run

Clone the repo and navigate to this folder:

```bash
cd AI-Powered\ Visual\ Novel
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in this folder with your Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```

Start the app:

```bash
streamlit run app.py
```

## 🛠️ Tech Stack

- 🐍 Python
- 🌐 Streamlit
- 🤖 Google Gemini API (`google-genai`)
- 🗣️ Microsoft Edge TTS (`edge-tts`)
- 🖼️ Pollinations AI (image generation)
- 🔐 python-dotenv
