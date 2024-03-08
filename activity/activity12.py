def is_palindrome(word):
    return word == word[::-1]


def count_palindromes(words_list):
    palindrome_count = 0
    palindrome_words = []

    for word in words_list:
        if is_palindrome(word):
            palindrome_count += 1
            palindrome_words.append(word)
    return palindrome_count, palindrome_words


if __name__ == '__main__':
    try:
        words_input = input("Enter a list of words (space-separated): ")
        word_list = words_input.split()
        count, palindrome_words = count_palindromes(word_list)
        print("\nResults:")
        print(f"Total words: {len(word_list)}")
        print(f"Palindromes count: {count}")
        print("Palindrome words:", palindrome_words)

    except Exception as e:
        print(f"Error: {e}. Please enter a valid list of words.")
