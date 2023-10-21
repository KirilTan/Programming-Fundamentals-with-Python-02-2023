def ascii_between_two_characters(first_character: str, second_character: str) -> str:
    result = []
    for current_char in range(ord(first_character) + 1, ord(second_character)):
        result.append(chr(current_char))
    return result


char1 = input()
char2 = input()
print(" ".join(ascii_between_two_characters(char1, char2)))
