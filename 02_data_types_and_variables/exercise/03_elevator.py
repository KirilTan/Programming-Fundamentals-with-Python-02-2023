from math import ceil

people_to_carry = int(input())
capacity = int(input())

result = ceil(people_to_carry / capacity)

print(result)