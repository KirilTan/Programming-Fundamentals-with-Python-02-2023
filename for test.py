# Input
n = int(input())

# Calculations
for current_number in range(1, n + 1):
    current_number_as_string = str(current_number)
    digit_sum = 0
    for digit in current_number_as_string:
        digit_sum += int(digit)

# Special or not
    if digit_sum in [5, 7, 11]:
        is_special = True
    else:
        is_special = False

# Output
    print(f"{current_number} -> {is_special}")