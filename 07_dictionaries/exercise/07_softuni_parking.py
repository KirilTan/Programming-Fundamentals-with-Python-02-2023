num_of_inputs = int(input())

# Input and logic
parking_lot = {}
for _ in range(num_of_inputs):

    user_input = input().split()
    command = user_input[0]
    person = user_input[1]

    if command == "register":
        license_number = user_input[2]

        if person in parking_lot.keys():
            print(f"ERROR: already registered with plate number {parking_lot[person][0]}")
        elif person not in parking_lot.keys():
            parking_lot[person] = [license_number]
            print(f"{person} registered {license_number} successfully")

    elif command == "unregister":
        if person not in parking_lot.keys():
            print(f"ERROR: user {person} not found")
        elif person in parking_lot.keys():
            parking_lot.pop(person)
            print(f"{person} unregistered successfully")


# Output
for person, license_numbers in parking_lot.items():
    print(f"{person} => {license_numbers[0]}")
