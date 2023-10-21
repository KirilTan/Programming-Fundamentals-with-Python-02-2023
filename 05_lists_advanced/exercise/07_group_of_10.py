# Input
numbers = [int(s) for s in input().split(", ")]

# Logic
current_group_range = 10
while numbers:
    current_group = [number for number in numbers if number <= current_group_range]
    print(f"Group of {current_group_range}'s: {current_group}")
    current_group_range += 10
    numbers = [number for number in numbers if number not in current_group]
