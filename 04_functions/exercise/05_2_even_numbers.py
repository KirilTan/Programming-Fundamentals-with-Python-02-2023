def is_even(number: int) -> bool:
    return number % 2 == 0


my_list = [int(s) for s in input().split()]

result = list(filter(is_even, my_list))
print(result)
