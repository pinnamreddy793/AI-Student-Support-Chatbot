from chatbot import get_response

def test_admission():
    assert "admission" in get_response("How do I apply for admission?").lower()

def test_registration():
    assert "register" in get_response("How do I register?").lower()

def test_greeting():
    assert "welcome" in get_response("hello").lower()

def test_thanks():
    assert "welcome" in get_response("thank you").lower()

def test_unknown():
    assert "sorry" in get_response("abcdefgxyz").lower()
