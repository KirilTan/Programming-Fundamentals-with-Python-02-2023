def indices_of_even_numbers(list_of_numbers: list) -> list:
    """This function takes a list of numbers and returns a list of the indices of the even numbers in the list."""

    return [index for index, value in enumerate(list_of_numbers) if value % 2 == 0]


all_numbers = [int(x) for x in input().split(", ")]
print(indices_of_even_numbers(all_numbers))
