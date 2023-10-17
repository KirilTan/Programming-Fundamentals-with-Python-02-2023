def sum_even_and_odd(number: str) -> int and int:
    """
    Takes a number and returns the sum of all even numbers and odd numbers in that number.
    """
    number_as_list = list(number)

    sum_of_even_numbers = 0
    sum_of_odd_numbers = 0

    for current_number in number_as_list:
        if int(current_number) % 2 == 0:
            sum_of_even_numbers += int(current_number)
        else:
            sum_of_odd_numbers += int(current_number)

    return sum_of_even_numbers, sum_of_odd_numbers


input_number = input()

sum_even, sum_odd = sum_even_and_odd(input_number)

output_text = f"Odd sum = {sum_odd}, Even sum = {sum_even}"

print(output_text)
