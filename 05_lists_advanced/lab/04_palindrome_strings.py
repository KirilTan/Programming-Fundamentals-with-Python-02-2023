def find_all_palindromes(list_of_words: list) -> list:
    """This function takes a list of words and returns a list of all palindromes in the list."""
    return [word for word in list_of_words if word == word[::-1]]


def find_palindrome_count(word: str, list_of_words: list) -> int:
    """This function takes a word and returns the number of times that the words is present
    within a list of words"""

    return len([s for s in list_of_words if s == word])


# Input
all_words = input().split()
sought_palindrome = input()

# Output
all_palindromes = find_all_palindromes(all_words)
print(all_palindromes)

repetitions_of_sought_palindrome = find_palindrome_count(word=sought_palindrome,list_of_words=all_words)
print(f"Found palindrome {repetitions_of_sought_palindrome} times")
