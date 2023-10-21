my_list = [int(s) for s in input().split()]

result = list(filter(lambda x: x % 2 == 0, my_list))
print(result)
