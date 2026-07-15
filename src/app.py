#AI Student Support Chatbot
#app.py file acts as the platform for the user to interact on the browser

from flask import Flask, render_template, request
from chatbot import get_response
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""

    if request.method == "POST":
        user_input = request.form["message"]
        response = get_response(user_input)

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)

