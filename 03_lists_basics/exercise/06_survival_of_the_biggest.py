starting_list = [int(s) for s in input().split()]
number_of_numbers_removed = int(input())

list_after_corrections = starting_list.copy()

for _ in range(number_of_numbers_removed):
    list_after_corrections.remove(min(list_after_corrections))

print(*list_after_corrections, sep=", ")
