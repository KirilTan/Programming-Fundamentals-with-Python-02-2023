def number_classification(numbers_list: list) -> list:

    """
    This function takes in a list of numbers and returns a list that contains lists of the positive,
    negative, even, and odd numbers. Note: Zero is counted for a positive number
    """

    positive_numbers = []
    negative_numbers = []
    even_numbers = []
    odd_numbers = []

    # Check if numbers are positive or negative
    for number in numbers_list:
        if number >= 0:
            positive_numbers.append(number)
        else:
            negative_numbers.append(number)

    # Check if numbers are even or odd
    for number in numbers_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    return [positive_numbers, negative_numbers, even_numbers, odd_numbers]


# Input
input_list = [int(s) for s in input().split(", ")]

# Variables
output_matrix = number_classification(input_list)
positive_list, negative_list, even_list, odd_list = output_matrix

# Output
print(f"Positive: {', '.join(map(str, positive_list))}")
print(f"Negative: {', '.join(map(str, negative_list))}")
print(f"Even: {', '.join(map(str, even_list))}")
print(f"Odd: {', '.join(map(str, odd_list))}")
