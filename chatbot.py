from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Simple rule-based chatbot
def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input in ["hi", "hello"]:
        return "Hello there! How can I help you?"

    elif "how are you" in user_input:
        return "I'm just a program, but I'm doing great! How about you?"

    elif "your name" in user_input:
        return "I’m a simple Python Chatbot created with if-else rules."

    elif "time" in user_input:
        now = datetime.now()
        return f"Current time is {now.strftime('%H:%M:%S')}"

    elif "date" in user_input:
        today = datetime.today().date()
        return f"Today's date is {today}"

    elif "bye" in user_input:
        return "Goodbye! Have a nice day 😊"

    else:
        return "Sorry, I don’t understand that. Can you rephrase?"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_message = request.form["msg"]
    return jsonify({"response": chatbot_response(user_message)})

if __name__ == "__main__":
    app.run(debug=True)
