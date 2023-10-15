input_list = input().split()
input_str = input()

output_list = []
for current_number in input_list:

    current_number_sum = 0
    for i in current_number:
        current_number_sum += int(i)

    current_number_sum %= len(input_str)

    output_list.append(input_str[current_number_sum])
    input_str = input_str.replace(input_str[current_number_sum], '', 1)

print(*output_list, sep="")

