# Input
input_list = input().split()
input_str = input()

output_text = []
for current_number in input_list:
    current_number = int(current_number)
    if sum(current_number) > len(input_str):
        continue

    current_number_as_letter = chr(sum(current_number))
    input_str.remove(current_number_as_letter)
    output_text.append(current_number_as_letter)

print(*output_text)
