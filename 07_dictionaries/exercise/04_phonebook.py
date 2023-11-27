phonebook = {}

while True:
    user_input = input()

    # Exit loop and prepare for output
    if len(user_input) <= 2:
        num_of_outputs = int(user_input)
        break

    name, phone_number = user_input.split("-")
    phonebook[name] = phone_number

# Output
for _ in range(num_of_outputs):
    current_name_for_output = input()
    if current_name_for_output in phonebook:
        print(f"{current_name_for_output} -> {phonebook[current_name_for_output]}")
    else:
        print(f"Contact {current_name_for_output} does not exist.")
