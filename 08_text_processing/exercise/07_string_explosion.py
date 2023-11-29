def string_explosion(starting_string: str) -> str:
    """
    This function's task is to delete x characters, starting after the exploded character ('>').
    If uit finds another explosion mark ('>') while deleting characters,
    it adds the strength to the previous explosion.
    It does not delete the explosion character – '>'.
    """

    final_string = ""
    explosion_strength = 0

    for index in range(len(starting_string)):
        # Explosion
        if explosion_strength > 0 and starting_string[index] != ">":
            explosion_strength -= 1

        # Explosion mark
        elif starting_string[index] == ">":
            final_string += starting_string[index]
            explosion_strength += int(starting_string[index + 1])

        # No explosion & no explosion mark
        else:
            final_string += starting_string[index]

    return final_string


input_string = input()
print(string_explosion(input_string))
