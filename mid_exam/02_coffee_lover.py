# Input
available_coffee = input().split()
number_of_inputs = int(input())

# Logic
for current_command in range(1, number_of_inputs + 1):
    command = input().split()

    if command[0] == "Include":
        available_coffee.append(command[1])

    elif command[0] == "Remove":
        if command[1] == "first":
            for current_pop in range(int(command[2])):
                if available_coffee:
                    available_coffee.pop(0)
                else:
                    continue
        elif command[1] == "last":
            for current_pop in range(int(command[2])):
                if available_coffee:
                    available_coffee.pop()
                else:
                    continue

    elif command[0] == "Prefer":
        if len(available_coffee) > int(command[1]) and len(available_coffee) > len(command[2]):
            available_coffee[int(command[1])], available_coffee[int(command[2])] = available_coffee[int(command[2])], available_coffee[int(command[1])]

    elif command[0] == "Reverse":
        available_coffee.reverse()

# Output
print("Coffees: ")
print(*available_coffee)
