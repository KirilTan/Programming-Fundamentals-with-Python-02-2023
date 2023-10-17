def sum_even_and_odd(number: str) -> str:
    """
    Takes a number and returns the sum of all even numbers and odd numbers in that number.
    """
    number_as_list = list(number)

    even_numbers = []
    odd_numbers = []

    for current_number in number_as_list:
        if int(current_number) % 2 == 0:
            even_numbers.append(int(current_number))
        else:
            odd_numbers.append(int(current_number))

    sum_of_even_numbers = sum(even_numbers)
    sum_of_odd_numbers = sum(odd_numbers)

    output_text = f"Odd sum = {sum_of_odd_numbers}, Even sum = {sum_of_even_numbers}"

    return output_text


input_number = input()

print(sum_even_and_odd(input_number))
