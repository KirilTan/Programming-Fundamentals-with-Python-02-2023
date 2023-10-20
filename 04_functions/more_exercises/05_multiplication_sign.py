def multiplication_sign(a: int, b: int, c: int) -> str:
    """This functions checks if the multiplication of the 3 numbers is negative, positive, or  the sum is zero without
    multiplying the three numbers.

    Args:
        a (int): The first number.
        b (int): The second number.
        c (int): The third number.

    Returns:
        str: The result of the check.
    """

    if a == 0 or b == 0 or c == 0:
        return_text = "zero"
    elif a < 0 or b < 0 or c < 0:
        num_of_negatives = sum(s < 0 for s in [a, b, c])
        if num_of_negatives % 2 == 0:
            return_text = "positive"
        else:
            return_text = "negative"
    else:
        return_text = "positive"

    return return_text


# Take user input for the 3 numbers
num1 = int(input())
num2 = int(input())
num3 = int(input())

# Check multiplication sign
print(multiplication_sign(a=num1, b=num2, c=num3))
