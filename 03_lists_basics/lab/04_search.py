number_of_inputs = int(input())
magic_word = input()

all_strings = []
for _ in range(number_of_inputs):
    current_string_input = input()
    all_strings.append(current_string_input)

print(all_strings)

filtered_strings = []
for current_string in all_strings:
    if magic_word in current_string:
        filtered_strings.append(current_string)

print(filtered_strings)
