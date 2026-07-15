#AI Student Support Chatbot
#chatbot.py contains code to search thr keywords and show answer from faq

import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FAQ_FILE = os.path.join(BASE_DIR, "faq.json")


with open(FAQ_FILE, "r") as file:
    faq = json.load(file)


def get_response(question):
    question = question.lower()

    for item in faq:
        if item["keyword"] in question:
            return item["response"]

    return "Sorry, I could not find an answer. Please contact the student support office."
