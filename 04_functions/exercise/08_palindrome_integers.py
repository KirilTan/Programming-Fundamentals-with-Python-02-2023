def is_palindrome(number: str) -> bool:

    """Function to check if a number is a palindrome.
    A palindrome is a number that reads the same forwards and backwards."""

    return number == number[::-1]


# Input
input_list = input().split(", ")

# Output
for current_number in input_list:
    print(is_palindrome(current_number))
