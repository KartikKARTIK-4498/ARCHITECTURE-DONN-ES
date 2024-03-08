from activity.activity11 import decode_message

def test_decode_message_valid_input():
    result = decode_message("72 101 108 108 111")
    assert result == "Hello"

def test_decode_message_empty_input():
    result = decode_message("")
    assert result == ""

def test_decode_message_invalid_input():
    result = decode_message("72 invalid 108 111")
    assert result == "Invalid"

def test_decode_message_negative_numbers():
    result = decode_message("72 -101 108 111")
    assert result == "Invalid"

def test_decode_message_float_numbers():
    result = decode_message("72 101.5 108 111")
    assert result == "Invalid"
