# Customer Support Chatbot (Flask)

A beginner-friendly Flask chatbot website. The browser sends each message to `/chat` using JavaScript `fetch()`. Python generates the reply and returns JSON. There is no `input()` loop in the web request flow.

## Project structure

```text
Customer_Support_Chatbot_Flask/
├── app.py
├── selflearning.py
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

## Run on Windows / VS Code

1. Open this folder in VS Code (the folder containing `app.py`).
2. Open Terminal → New Terminal.
3. Optional but recommended: create a virtual environment:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

4. Install packages:

   ```powershell
   py -m pip install -r requirements.txt
   ```

5. Start Flask:

   ```powershell
   py app.py
   ```

6. Open **http://127.0.0.1:5000** in Chrome. Do not open `templates/index.html` directly and do not use VS Code Live Server (port 5500) for this Flask app.

Expected terminal output includes:

```text
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

Test API status at **http://127.0.0.1:5000/health**.

## Important

- Keep `app.py`, `selflearning.py`, `templates/`, and `static/` together in the same project folder.
- The old console `greet()` / `chat()` functions using `input()` are not needed for the web app. This version replaces them with a `match_reply(message)` method that returns a response.
- The replies are keyword/rule-based, not a trained or generative AI model. Connect an AI API separately if you want open-ended AI answers.
- `debug=True` is for local development only. For a production deployment, use a production WSGI server such as Waitress and configure the host/port as required by your host.
