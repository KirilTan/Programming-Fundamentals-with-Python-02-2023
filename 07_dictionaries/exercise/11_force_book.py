command = input()

database = {}
while command != "Lumpawaroo":

    if "|" in command:
        force_side, force_user = command.split(" | ")

        # Check if the user is present in the list of users
        is_present = False
        for value in database.values():
            if force_user in value:
                is_present = True
                break

        # If the user is not present in the list of users, add it to the list of users
        if not is_present:
            if force_side not in database.keys():
                database[force_side] = []
            database[force_side].append(force_user)

    if "->" in command:
        force_user, force_side = command.split(" -> ")

        # Remove the user from original side
        for value in database.values():
            if force_user in value:
                value.remove(force_user)
                break

        # Add the user to the new side
        if force_side not in database.keys():
            database[force_side] = []
        database[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

    command = input()

for force_side, force_users in database.items():
    if force_users:
        print(f"Side: {force_side}, Members: {len(force_users)}")
        for force_user in force_users:
            print(f"! {force_user}")
