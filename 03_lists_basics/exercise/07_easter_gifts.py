# Input
planned_gifts = input().split()

# Calculations
command = input()
while command != "No Money":

    command_as_list = command.split()
    action = command_as_list[0]
    current_gift = command_as_list[1]

    if action == "OutOfStock":
        planned_gifts = [None if x == current_gift else x for x in planned_gifts]
        # while index < len(planned_gifts):
        #     if planned_gifts[index] == current_gift:
        #         planned_gifts[index] = None
        #     index += 1
    elif action == "Required":
        required_gift_index = int(command_as_list[2])
        if 0 <= required_gift_index < len(planned_gifts):
            planned_gifts[required_gift_index] = current_gift

    elif action == "JustInCase":
        planned_gifts[-1] = current_gift  # planned_gifts.pop()
        # planned_gifts.pop()
        # planned_gifts.append(current_gift)

    command = input()

# Output
filtered_planned_gifts = [x for x in planned_gifts if x is not None]
print(*filtered_planned_gifts)
