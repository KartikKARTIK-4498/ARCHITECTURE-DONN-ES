from activity.activity1 import count_upper_lower

def test_count_upper_lower_mixed_case():
    result = count_upper_lower("HelloWorld")
    assert result == (2, 8)

def test_count_upper_lower_all_uppercase():
    result = count_upper_lower("HELLO")
    assert result == (5, 0)

def test_count_upper_lower_all_lowercase():
    result = count_upper_lower("hello")
    assert result == (0, 5)

def test_count_upper_lower_empty_string():
    result = count_upper_lower("")
    assert result == (0, 0)
