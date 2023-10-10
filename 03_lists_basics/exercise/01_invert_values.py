numbers = input().split()

reversed_numbers = []
for number in numbers:
    current_number = int(number)
    reversed_numbers.append(-current_number)

print(reversed_numbers)
