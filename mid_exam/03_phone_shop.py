phone_models = input().split(", ")

command = input().split(" - ")
while command[0] != "End":

    if command[0] == "Add":
        if command[1] not in phone_models:
            phone_models.append(command[1])

    elif command[0] == "Remove":
        if command[1] in phone_models:
            phone_models.remove(command[1])

    elif command[0] == "Bonus phone":
        bonus_command_parts = command[1].split(":")
        if bonus_command_parts[0] in phone_models:
            old_phone_location = phone_models.index(bonus_command_parts[0])
            phone_models.insert(old_phone_location + 1, bonus_command_parts[1])

    elif command[0] == "Last":
        if command[1] in phone_models:
            phone_model = command[1]
            phone_model_location = phone_models.index(phone_model)
            phone_model = phone_models.pop(phone_model_location)
            phone_models.append(phone_model)

    command = input().split(" - ")

print(", ".join(phone_models))
