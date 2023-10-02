number_of_inputs = int(input())
response = ""


for _ in range(number_of_inputs):

    current_input = int(input())

    if current_input == 88:
        response = "Hello"
    elif current_input == 86:
        response = "How are you?"
    elif current_input != 88 and current_input != 86 and current_input < 88:
        response = "GREAT!"
    elif current_input > 88:
        response = "Bye."

    print(response)
