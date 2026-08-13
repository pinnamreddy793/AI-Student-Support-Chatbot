#AI Student Support Chatbot
#chatbot.py contains code to search keywords and show answer from faq

import json
import os
from datetime import datetime
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Ensure required NLTK resources are available
try:
    nltk.data.find("tokenizers/punkt_tab")
except LookupError:
    nltk.download("punkt_tab")

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FAQ_FILE = os.path.join(BASE_DIR, "faq.json")

with open(FAQ_FILE, "r") as file:
    faq = json.load(file)

question_count = 0


def preprocess(text):
    """
    Preprocess user input using basic NLP.
    - Convert to lowercase
    - Tokenize the sentence
    - Remove punctuation
    - Remove English stop words
    """

    text = text.lower()

    tokens = word_tokenize(text)

    stop_words = set(stopwords.words("english"))

    tokens = [
        word for word in tokens
        if word.isalnum() and word not in stop_words
    ]

    return tokens


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

    # NLP preprocessing
    tokens = preprocess(question)

    best_match = None
    highest_score = 0


    for item in faq:

        #score = 0

        for keyword in item["keywords"]:

            keyword = keyword.lower()
            score = 0

            #Exact keyword matching
            if keyword in tokens:
                score += 3

            #Keyword appears in sentence
            if keyword in question:
                score += 2

            #Handle similar words
            for token in tokens:

                if keyword in token or token in keyword:
                    score += 1


            if score > highest_score:
                highest_score = score
                best_match = item

    #Return best matching FAQ response
    if best_match and highest_score > 0:
        return best_match["response"]


    return (
        "Sorry, I could not understand your question.\n\n"
        "Please try asking about admissions, registration, tuition, "
        "financial aid, scholarships, housing, library, transcripts, "
        "or graduation."
    )


def get_question_count():

    return question_count
