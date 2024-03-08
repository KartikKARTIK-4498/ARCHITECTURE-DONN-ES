from activity.activity2 import extract_word_python, extract_word_learn, extract_phrase_programming_language, reverse_string

def test_extract_word_python():
    text = "Python is a powerful and easy-to-learn programming language."
    result = extract_word_python(text)
    assert result == "Python"

def test_extract_word_learn():
    text = "Python is a powerful and easy-to-learn programming language."
    result = extract_word_learn(text)
    assert result == "easy-to-learn"

def test_extract_phrase_programming_language():
    text = "Python is a powerful and easy-to-learn programming language."
    result = extract_phrase_programming_language(text)
    assert result == "programming language"

def test_reverse_string():
    text = "Python is a powerful and easy-to-learn programming language."
    result = reverse_string(text)
    assert result == ".egaugnal gnimmargorp nrael-ot-ysae dna lufrewop a si nohtyP"

