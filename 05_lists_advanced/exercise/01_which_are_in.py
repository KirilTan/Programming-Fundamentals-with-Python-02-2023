first_sequence = input().split(", ")
second_sequence = input().split(", ")

new_sequence = []
for current_sequence in first_sequence:
    for current_element in second_sequence:
        if current_sequence in current_element:
            new_sequence.append(current_sequence)
            break

print(new_sequence)
