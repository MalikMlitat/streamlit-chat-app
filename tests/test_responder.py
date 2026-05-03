from chat_app import generate_response


def test_response_contains_original_message():
    response = generate_response("hello")
    assert "hello" in response


def test_response_contains_reversed_message():
    response = generate_response("hello")
    assert "olleh" in response


def test_empty_string():
    response = generate_response("")
    assert isinstance(response, str)


def test_returns_string():
    response = generate_response("test input")
    assert isinstance(response, str)
