def string_multiplication(str1: str, str2: str) -> int:
    """
    This function returns the sum of the multiplied character codes of the two strings.
    If one of the strings is longer than the other,
    it adds the remaining character codes to the total sum without multiplication.
    """
    total_sum = 0

    if len(str1) > len(str2):
        for char in str1[len(str2):]:
            total_sum += ord(char)

    elif len(str1) < len(str2):
        for char in str2[len(str1):]:
            total_sum += ord(char)

    for char1, char2 in zip(str1, str2):
        total_sum += ord(char1) * ord(char2)

    return total_sum


first_string, second_string = input().split()

print(string_multiplication(first_string, second_string))