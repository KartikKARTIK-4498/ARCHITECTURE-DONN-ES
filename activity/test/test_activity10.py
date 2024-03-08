from activity.activity10 import find_largest_number

def test_find_largest_number_positive_numbers():
    result = find_largest_number(10, 20, 15)
    assert result == 20

def test_find_largest_number_negative_numbers():
    result = find_largest_number(-5, -8, -3)
    assert result == -3

def test_find_largest_number_mixed_numbers():
    result = find_largest_number(-10, 5, 0)
    assert result == 5

def test_find_largest_number_equal_numbers():
    result = find_largest_number(7, 7, 7)
    assert result == 7
