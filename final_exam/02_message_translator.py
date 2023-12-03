import re

regex = r"!([A-Z][a-z]{2,})!:\[([A-Za-z\s]{8,})\]"

results = []
number_of_inputs = int(input())
for _ in range(number_of_inputs):
    input_string = input()
    match = re.search(regex, input_string)

    if match:

        message = match.group(1)
        key = match.group(2)
        key = key.replace(" ", "")

        print(f"{message}: ", end="")
        for letter in key:
            print(ord(letter), end=" ")

    else:
        print("\nThe message is invalid")
