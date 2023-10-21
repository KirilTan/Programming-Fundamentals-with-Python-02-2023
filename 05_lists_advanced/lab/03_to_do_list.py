def sort_activities(list_of_activities: list) -> list:

    """This function takes a list of activities and returns a sorted list of activities based on their
    importance value. The importance value is the [0] index of the current activity in the list."""

    sorted_activities = sorted(list_of_activities, key=lambda x: int(x.split("-")[0]))
    sorted_activities = [current_activity.split("-")[1] for current_activity in sorted_activities]

    return sorted_activities


activities = []
while True:

    command = input()

    if command == "End":
        break
    else:
        activities.append(command)

print(sort_activities(activities))
