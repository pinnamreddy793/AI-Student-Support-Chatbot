from chatbot import get_response, preprocess
import os


# -------------------------------
# FAQ Category Tests
# -------------------------------

def test_admission():
    response = get_response("How do I apply for admission?")
    assert "admission" in response.lower()


def test_registration():
    response = get_response("How do I register for classes?")
    assert "registration" in response.lower()


def test_course():
    response = get_response("Where can I see available courses?")
    assert "course" in response.lower()


def test_advisor():
    response = get_response("How can I contact my academic advisor?")
    assert "advisor" in response.lower()


def test_tuition():
    response = get_response("How much is tuition?")
    assert "tuition" in response.lower()


def test_payment():
    response = get_response("How can I make my tuition payment?")
    assert "payment" in response.lower()


def test_financial_aid():
    response = get_response("How can I get financial aid?")
    assert "financial aid" in response.lower() or "financial" in response.lower()


def test_scholarship():
    response = get_response("Are scholarships available?")
    assert "scholarship" in response.lower()


def test_student_loan():
    response = get_response("I need information about student loans")
    assert "loan" in response.lower()


def test_housing():
    response = get_response("Tell me about student housing?")
    assert "housing" in response.lower() or "student housing" in response.lower() or "accomodation" in response.lower()


def test_library():
    response = get_response("What are the library hours?")
    assert "library" in response.lower()


def test_book():
    response = get_response("How can I borrow a book?")
    assert "book" in response.lower()


def test_parking():
    response = get_response("Where can I get a parking permit?")
    assert "parking" in response.lower()


def test_transcript():
    response = get_response("How do I request my transcript?")
    assert "transcript" in response.lower()


def test_graduation():
    response = get_response("What are the graduation requirements?")
    assert "graduation" in response.lower()


def test_email():
    response = get_response("How do I access my university email?")
    assert "email" in response.lower()


def test_password():
    response = get_response("I forgot my password")
    assert "password" in response.lower()


def test_wifi():
    response = get_response("How do I connect to campus wifi?")
    assert "wi-fi" in response.lower() or "wifi" in response.lower()


def test_it_support():
    response = get_response("I need IT support")
    assert "it" in response.lower()


def test_student_id():
    response = get_response("Where can I get my student ID?")
    assert "student id" in response.lower() or "id" in response.lower()


def test_international_student():
    response = get_response("I am an international student")
    assert "international" in response.lower()


def test_career():
    response = get_response("Does the university provide career services?")
    assert "career" in response.lower()


def test_internship():
    response = get_response("Where can I find internships?")
    assert "internship" in response.lower()

def test_internship_variation():
    response = get_response("How can I apply for student housing")
    assert "internship" in response.lower()

def test_health_services():
    response = get_response("Where can I find health services?")
    assert "health" in response.lower()


def test_cafeteria():
    response = get_response("Where is the cafeteria?")
    assert "cafeteria" in response.lower()



# -------------------------------
# NLP Processing Tests
# -------------------------------

def test_lowercase_conversion():
    tokens = preprocess("ADMISSION APPLICATION")
    assert "admission" in tokens

def test_application_variation():
    response = get_response(
        "Where can I submit my application?"
    )
    assert "application" in response.lower()


def test_course_plural():
    response = get_response(
        "Where can I see available courses?"
    )
    assert "course" in response.lower()


def test_wifi_variation():
    response = get_response(
        "How do I connect to campus wifi?"
    )
    assert "wifi" in response.lower() or "wi-fi" in response.lower()


def test_payment_question():
    response = get_response(
        "How do I make tuition payment?"
    )
    assert "payment" in response.lower()


def test_password_reset():
    response = get_response(
        "I forgot my password"
    )
    assert "password" in response.lower()


def test_financial_aid():
    response = get_response(
        "How can I apply for financial aid?"
    )
    assert "financial" in response.lower() or "financial aid" in response.lower()


def test_tokenization():
    tokens = preprocess("How do I register for classes?")
    assert "register" in tokens


def test_stopword_removal():
    tokens = preprocess("How do I apply for admission")
    assert "do" not in tokens


def test_response_not_empty():
    response = get_response("Tell me about tuition")
    assert len(response) > 0



# -------------------------------
# Conversation Tests
# -------------------------------

def test_greeting():
    response = get_response("hello")
    assert "welcome" in response.lower()


def test_thanks():
    response = get_response("thank you")
    assert "welcome" in response.lower()


def test_goodbye():
    response = get_response("bye")
    assert "thank you" in response.lower()


def test_unknown_question():
    response = get_response("xyzabc123")
    assert "sorry" in response.lower()



# -------------------------------
# File Validation Test
# -------------------------------

def test_faq_file_exists():
    assert os.path.exists("faq.json")
