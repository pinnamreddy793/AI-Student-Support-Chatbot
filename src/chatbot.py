#AI Student Support Chatbot
#chatbot.py contains code to search thr keywords and show answer from faq

import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FAQ_FILE = os.path.join(BASE_DIR, "faq.json")

with open(FAQ_FILE, "r") as file:
    faq = json.load(file)

question_count = 0


def log_question(question):

    logfile = os.path.join(BASE_DIR, "chatlog.txt")

    with open(logfile, "a") as log:

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log.write(f"[{timestamp}] {question}\n")


def get_response(question):

    global question_count

    question_count += 1

    log_question(question)

    question = question.lower().strip()

    greetings = [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ]

    if question in greetings:

        return (
            "Hello! Welcome to the AI Student Support Chatbot. "
            "How may I assist you today?"
        )

    if "thank" in question:

        return (
            "You're welcome! "
            "I'm always happy to help."
        )

    if "bye" in question or "goodbye" in question:

        return (
            "Thank you for using the AI Student Support Chatbot. "
            "Have a wonderful day!"
        )

    if "who are you" in question:

        return (
            "I am an AI Student Support Chatbot designed to help students "
            "with admissions, registration, tuition, financial aid, and "
            "other university services."
        )

    if "help" in question:

        return (
            "You can ask me about:\n"
            "- Admissions\n"
            "- Registration\n"
            "- Tuition\n"
            "- Financial Aid\n"
            "- Scholarships\n"
            "- Housing\n"
            "- Library\n"
            "- Graduation\n"
            "- Transcripts\n"
            "- Academic Advising"
        )

    words = question.split()

    for item in faq:

        keyword = item["keyword"].lower()

        if keyword in question:

            return item["response"]

        for word in words:

            if word == keyword:

                return item["response"]

    return (
        "Sorry, I could not understand your question.\n\n"
        "Please try asking about admissions, registration, tuition, "
        "financial aid, scholarships, housing, library, transcripts, "
        "or graduation."
    )


def get_question_count():

    return question_count
