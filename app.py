from flask import Flask, jsonify
import random


app = Flask(__name__)

quotes = [
   "DevOps, c'est la collaboration avant tout",
   "Automatise ce qui peut l'être, surveille ce qui doit l'être.",
   "Livrer petit et souvent, c'est livrer mieux."
]

@app.route("/")
def home():
    return "Hello DevOps!"

@app.route("/quote")
def get_quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

