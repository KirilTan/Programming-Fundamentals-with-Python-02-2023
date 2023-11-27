command = input()

while command != "end":

    text = command

    print(f"{text} = {text[::-1]}")

    command = input()
