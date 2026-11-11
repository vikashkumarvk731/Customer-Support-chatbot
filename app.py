from flask import Flask, jsonify, render_template, request
from selflearning import SupportBot

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
bot = SupportBot()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    user_message = str(data.get("message", "")).strip()

    if not user_message:
        return jsonify({"reply": "Please enter a message."}), 400
    if len(user_message) > 1000:
        return jsonify({"reply": "Please keep your message under 1000 characters."}), 400

    reply = bot.match_reply(user_message)
    return jsonify({"reply": reply})


@app.route("/health")
def health():
    return jsonify({"status": "ok", "message": "Customer Support Chatbot is running."})


if __name__ == "__main__":
    # debug=True is for local development only. Do not use the Flask dev server in production.
    app.run(host="127.0.0.1", port=5000, debug=True)
