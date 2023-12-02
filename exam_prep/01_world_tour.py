# Input
destinations = input()
command = input().split(":")

# Logic
while command[0] != "Travel":

    if command[0] == "Add Stop":
        index, string = int(command[1]), command[2]
        if index in range(len(destinations)):
            destinations = destinations[:index] + string + destinations[index:]

    elif command[0] == "Remove Stop":
        start_index, end_index = int(command[1]), int(command[2])
        if end_index in range(len(destinations)):
            destinations = destinations[:start_index] + destinations[end_index + 1:]

    elif command[0] == "Switch":
        old_string, new_string = command[1], command[2]
        if old_string in destinations:
            destinations = destinations.replace(old_string, new_string)

    print(destinations)
    command = input().split(":")

# Output
print(f"Ready for world tour! Planned stops: {destinations}")
