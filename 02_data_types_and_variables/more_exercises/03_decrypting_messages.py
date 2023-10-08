key = int(input())
number_of_inputs = int(input())

result_characters = []

for _ in range(number_of_inputs):
    current_input = str(input())
    current_input_value_after_key = key + ord(current_input)
    result_characters.append(chr(current_input_value_after_key))

final_string = ''.join(result_characters)
print(final_string)
