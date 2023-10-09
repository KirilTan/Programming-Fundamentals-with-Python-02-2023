number_of_inputs = int(input())

positive_numbers = []
negative_numbers = []

for _ in range(number_of_inputs):
    current_input = int(input())

    if current_input >= 0:
        positive_numbers.append(current_input)
    elif current_input < 0:
        negative_numbers.append(current_input)

print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {len(positive_numbers)}")
print(f"Sum of negatives: {sum(negative_numbers)}")
