def is_even(number: int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False


my_list = [int(s) for s in input().split()]

result = list(filter(is_even, my_list))
print(result)
