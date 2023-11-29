def length_validator(username: str) -> bool:
    """
    This validator checks if the username is between 3 and 16 characters long, inclusive.
    """
    if 3 <= len(username) <= 16:
        return True
    return False


def characters_validator(username: str) -> bool:
    """
    This validator confirms that the username contains only letters, numbers, hyphens, and underscores
    """
    for character in username:
        if not (character.isalnum() or character == "-" or character == "_"):
            return False
    return True


def redundant_symbols_validator(username: str) -> bool:
    """
    This validator confirms that the username does not contain any spaces.
    """
    if " " in username:
        return False
    return True


def username_is_valid(username: str) -> bool:
    """
    This validator confirms that the username is valid.
    """
    if (length_validator(username)
            and characters_validator(username)
            and redundant_symbols_validator(username)):
        return True
    return False


all_usernames = input().split(", ")

for current_username in all_usernames:
    if username_is_valid(current_username):
        print(current_username)
