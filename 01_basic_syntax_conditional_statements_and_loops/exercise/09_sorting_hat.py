command = input()

while True:

    if command == "Welcome!":
        print("Welcome to Hogwarts.")
        break

    current_name = command

    if current_name == "Voldemort":
        print("You must not speak of that name!")
        break
    elif len(current_name) < 5:
        print(f"{current_name} goes to Gryffindor.")
    elif len(current_name) == 5:
        print(f"{current_name} goes to Slytherin.")
    elif len(current_name) == 6:
        print(f"{current_name} goes to Ravenclaw.")
    elif len(current_name) > 6:
        print(f"{current_name} goes to Hufflepuff.")

    command = input()