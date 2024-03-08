from activity.activity13 import is_palindrome, count_palindromes

def test_is_palindrome_true():
    assert is_palindrome("radar") is True

def test_is_palindrome_false():
    assert is_palindrome("python") is False

def test_count_palindromes_empty_input():
    result = count_palindromes([])
    assert result == 0

def test_count_palindromes_no_palindromes():
    result = count_palindromes(["hello", "world", "python"])
    assert result == 0

def test_count_palindromes_some_palindromes():
    result = count_palindromes(["level", "deed", "hello", "radar"])
    assert result == 3

def test_count_palindromes_all_palindromes():
    result = count_palindromes(["madam", "racecar", "level", "deed"])
    assert result == 4
