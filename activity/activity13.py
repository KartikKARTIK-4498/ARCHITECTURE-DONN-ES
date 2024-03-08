def is_palindrome(word):
    return word == word[::-1]


def count_palindromes(words_list):
    palindrome_count = 0

    for word in words_list:
        if is_palindrome(word):
            palindrome_count += 1

    return palindrome_count


if __name__ == '__main__':
    try:
        words_input = input("Enter a list of words (space-separated): ")
        word_list = words_input.split()
        count = count_palindromes(word_list)
        print("\nResults:")
        print(f"Total words: {len(word_list)}")
        print(f"Palindromes count: {count}")

    except Exception as e:
        print(f"Error: {e}. Please enter a valid list of words.")
