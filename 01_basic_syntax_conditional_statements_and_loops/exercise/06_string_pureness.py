number_of_inputs = int(input())

for _ in range(number_of_inputs):

    current_input = input()

    if "," in current_input or \
        "." in current_input or \
        "_" in current_input:
        print(f"{current_input} is not pure!")
    else:
        print(f"{current_input} is pure.")
