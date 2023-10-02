command = input()

while command != "End":

    if command != "SoftUni":
        new_string = ""
        for character in command:
            new_string += character * 2
        print(new_string)

    command = input()