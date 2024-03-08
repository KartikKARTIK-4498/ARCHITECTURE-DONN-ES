from activity.activity8 import guess_the_number
from unittest.mock import patch

def test_guess_the_number_incorrect_guess():
    with patch('builtins.input', side_effect=['50', '75', '88', '92', '95']):
        result = guess_the_number()
    assert result is False

def test_guess_the_number_invalid_input_then_correct_guess():
    with patch('builtins.input', side_effect=['invalid', '42']):
        result = guess_the_number()
    assert result == "error"

def test_guess_the_number_out_of_attempts():
    with patch('builtins.input', side_effect=['10', '20', '30', '40', '50']):
        result = guess_the_number()
    assert result is False
