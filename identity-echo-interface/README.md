# Identity Echo Interface

An interactive Streamlit app that collects a user's name and message, validates the inputs with conditional routing, and echoes back a formatted confirmation along with a token cost estimate.

---

## Features

- **Multi-field input** — collects Name and Message via text inputs
- **Conditional validation** — shows targeted error/warning messages for missing fields
- **Formatted echo** — displays a success message with the user's name and message
- **Token cost estimator** — approximates token consumption using a character-based heuristic (chars ÷ 4)

---

## How to Run

1. **Clone the repo** and navigate to this folder:
   ```bash
   cd identity-echo-interface
   ```

2. **Install Streamlit** (the only dependency):
   ```bash
   pip install streamlit
   ```

3. **Start the app:**
   ```bash
   streamlit run app.py
   ```

---

## Tech Stack

- Python
- Streamlit
