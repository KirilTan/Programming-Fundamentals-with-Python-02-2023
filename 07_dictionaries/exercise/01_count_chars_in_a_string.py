# Code to remove whitespace
def remove_whitespaces(string):
    """
    This function removes all whitespaces from a string.
    :param string:
    :return string:
    """
    return string.replace(" ", "")


# User input
input_string = input()
input_string = remove_whitespaces(input_string)

# Count occurrences of each letter
occurrences = {}
for letter in input_string:
    if letter in occurrences:
        occurrences[letter] += 1
    else:
        occurrences[letter] = 1

# Output
for current_letter, occurrences_of_current_letter in occurrences.items():
    print(f"{current_letter} -> {occurrences_of_current_letter}")
