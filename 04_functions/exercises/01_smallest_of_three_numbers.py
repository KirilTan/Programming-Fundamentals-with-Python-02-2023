def smallest_number(some_list:list) -> int:
    return min(some_list)


input_list = [int(input()) for _ in range(3)]

print(smallest_number(input_list))
