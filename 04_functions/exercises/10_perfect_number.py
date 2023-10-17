def is_perfect(number: int) -> bool:

    """Function to check if a number is a perfect number.
    A perfect number is a number that is equal to the sum of its proper divisors."""

    divisors_sum = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            divisors_sum += divisor

    return divisors_sum == number


# Input
input_number = int(input())

# Output
if is_perfect(input_number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
