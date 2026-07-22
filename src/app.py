#AI Student Support Chatbot
#app.py file acts as the platform for the user to interact on the browser


from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session
)

from chatbot import get_response
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

# Secret key for session management
app.secret_key = "student_support_chatbot_secret"

# Demo user credentials
USERNAME = "student"
PASSWORD = "password123"


@app.route("/")
def home():

    if "user" not in session:
        return redirect(url_for("login"))

    if "chat_history" not in session:
        session["chat_history"] = []

    return render_template(
        "index.html",
        username=session["user"],
        chat_history=session["chat_history"]
    )


@app.route("/chat", methods=["POST"])
def chat():

    if "user" not in session:
        return redirect(url_for("login"))

    message = request.form.get("message")

    if message:

        response = get_response(message)

        history = session.get("chat_history", [])

        history.append({
            "user": message,
            "bot": response
        })

        session["chat_history"] = history

    return redirect(url_for("home"))


@app.route("/clear")
def clear():

    if "chat_history" in session:
        session["chat_history"] = []

    return redirect(url_for("home"))


@app.route("/login", methods=["GET", "POST"])
def login():

    error = ""

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == USERNAME and password == PASSWORD:

            session["user"] = username
            session["chat_history"] = []

            return redirect(url_for("home"))

        else:
            error = "Invalid username or password."

    return render_template("login.html", error=error)


@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
