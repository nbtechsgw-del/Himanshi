from flask import Flask, render_template, request, jsonify
import json
from difflib import get_close_matches

app = Flask(__name__)

def load_faqs():
    with open("faqs.json", "r", encoding="utf-8") as file:
        return json.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_question = request.json.get("question", "").lower()
    faqs = load_faqs()

    questions = [faq["question"].lower() for faq in faqs]

    match = get_close_matches(user_question, questions, n=1, cutoff=0.4)

    if match:
        for faq in faqs:
            if faq["question"].lower() == match[0]:
                return jsonify({"answer": faq["answer"]})

    return jsonify({"answer": "Sorry, I could not find a relevant answer. Please contact the company support team."})

if __name__ == "__main__":
    app.run(debug=True)