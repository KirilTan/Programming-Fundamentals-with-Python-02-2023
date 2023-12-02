import re

regex = r"@#{1,}[A-Z][A-Za-z0-9]{4,}[A-Z]@#{1,}"

num_of_inputs = int(input())

for _ in range(num_of_inputs):
    input_string = input()
    match = re.findall(regex, input_string)

    if match:
        group = ""
        for current_symbol in match[0]:
            if current_symbol.isdigit():
                group += current_symbol

        if group == "":
            group = "00"

        print(f"Product group: {group}")

    else:
        print("Invalid barcode")