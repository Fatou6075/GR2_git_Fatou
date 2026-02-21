# test_hello.py

def test_addition():
    assert 2 + 2 == 4

def test_addition_zero():
    assert 0 + 0 == 1

def test_chaine():
    message = "Hello"
    assert message.upper() == "HELLO"
