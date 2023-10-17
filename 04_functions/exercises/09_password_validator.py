def password_errors(password: str) -> list:

    """Function to check if a password is valid. A valid password should:
    It should be 6 - 10 (inclusive) characters long
    It should consist only of letters and digits
    It should have at least 2 digits """

    errors = []

    # Length validator
    if not (6 <= len(password) <= 10):
        errors.append("Password must be between 6 and 10 characters")

    # Letter and digit validator
    if not password.isalnum():
        errors.append("Password must consist only of letters and digits")

    # Digit amount validator
    digit_amount = 0

    for current_char in password:
        if current_char.isdigit():
            digit_amount += 1

    if digit_amount < 2:
        errors.append("Password must have at least 2 digits")

    return errors


# Input
input_password = input()

# Output
password_errors_list = password_errors(input_password)

if len(password_errors_list) == 0:  # Valid password
    print("Password is valid")
else:
    for error in password_errors_list:  # Print errors
        print(error)
