# Input
n = int(input())

# Calculations
for current_number in range(1, n + 1):
    current_number_as_string = str(current_number)
    digits_sum = 0
    for digit in current_number_as_string:
        digits_sum += int(digit)
    is_special = False
    if digits_sum in [5, 7, 11]:
        is_special = True

# Output
    print(f"{current_number} -> {is_special}")
