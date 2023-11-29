def encrypt(message: str) -> str:
    """
    This function returns the encrypted version the given message.
    It encrypts the text by replacing each character with the corresponding
    character three positions forward in the ASCII table
    """

    encrypted_message = ""

    for char in message:
        encrypted_message += chr(ord(char) + 3)

    return encrypted_message


input_message = input()

print(encrypt(input_message))