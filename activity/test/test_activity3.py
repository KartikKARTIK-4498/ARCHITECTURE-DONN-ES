from activity.activity3 import add_two_numbers
import builtins
from unittest.mock import patch

def test_add_two_numbers_valid_input():
    with patch.object(builtins, 'input', side_effect=['5', '7']):
        result = add_two_numbers()
    assert result == 12

def test_add_two_numbers_invalid_input():
    with patch.object(builtins, 'input', side_effect=['abc', '7']):
        result = add_two_numbers()
    assert result is None

def test_add_two_numbers_negative_input():
    with patch.object(builtins, 'input', side_effect=['-5', '7']):
        result = add_two_numbers()
    assert result == 2
