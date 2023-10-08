# Inputs
number_of_inputs = int(input())

# Check if balanced or not
is_balanced = True
last_bracket = ""
for _ in range(number_of_inputs):
    current_input = input()
    if current_input not in ["(", ")"]:
        continue

    if last_bracket == "" and current_input == ")" or last_bracket == current_input:
        is_balanced = False
        break

    last_bracket = current_input

# Output
if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
