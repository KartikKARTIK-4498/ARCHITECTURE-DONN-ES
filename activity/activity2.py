def extract_word_python(text):
    return text.split()[0]


def extract_word_learn(text):
    return text.split()[-3]


def extract_phrase_programming_language(text):
    start_index = text.find("programming")
    end_index = text.find("language") + len("language")
    return text[start_index:end_index]


def reverse_string(text):
    return text[::-1]


text = "Python is a powerful and easy-to-learn programming language."

result_extract_word_python = extract_word_python(text)
result_extract_word_learn = extract_word_learn(text)
result_extract_phrase = extract_phrase_programming_language(text)
result_reverse_string = reverse_string(text)

print("1. Extracted word 'Python':", result_extract_word_python)
print("2. Extracted word 'learn':", result_extract_word_learn)
print("3. Extracted phrase 'programming language':", result_extract_phrase)
print("4. Reversed string:", result_reverse_string)
