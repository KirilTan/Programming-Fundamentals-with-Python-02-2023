schedule = input().split(", ")

command = input().split(":")
while not command[0] == "course start":

    if command[0] == "Add":  # Add the lesson to the end of the schedule if it does not exist.
        lesson = command[1]
        if lesson not in schedule:
            schedule.append(lesson)

    elif command[0] == "Insert":  # Insert the lesson to the given index, if it does not exist.
        lesson, index = command[1], int(command[2])
        if lesson not in schedule:
            schedule.insert(index, lesson)

    elif command[0] == "Remove":  # Remove the lesson, if it exists
        lesson = command[1]
        if lesson in schedule:
            schedule.remove(lesson)

    elif command[0] == "Swap":  # Swap the position of the two lessons if they exist
        lesson_1, lesson_2 = command[1], command[2]
        if lesson_1 in schedule and lesson_2 in schedule:
            index_1, index_2 = schedule.index(lesson_1), schedule.index(lesson_2)
            schedule[index_1], schedule[index_2] = schedule[index_2], schedule[index_1]

        # Move exercises next to lessons if they exist
        exercise_1 = f"{lesson_1}-Exercise"
        exercise_2 = f"{lesson_2}-Exercise"
        if exercise_1 in schedule and exercise_2 not in schedule:
            schedule.pop(schedule.index(exercise_1))
            schedule.insert(schedule.index(lesson_1) + 1, exercise_1)
        elif exercise_2 in schedule and exercise_1 not in schedule:
            schedule.pop(schedule.index(exercise_2))
            schedule.insert(schedule.index(lesson_2) + 1, exercise_2)
        elif exercise_1 in schedule and exercise_2 in schedule:
            schedule.pop(schedule.index(exercise_1))
            schedule.pop(schedule.index(exercise_2))
            schedule.insert(schedule.index(lesson_1) + 1, exercise_1)
            schedule.insert(schedule.index(lesson_2) + 1, exercise_2)

    elif command[0] == "Exercise":  # Add Exercise in the schedule right after the lesson index
        lesson = command[1]
        exercise = f"{lesson}-Exercise"

        if lesson not in schedule and exercise not in schedule:  # If the lesson doesn't exist, add the lesson at the
            # end of the course schedule, followed by the Exercise.
            schedule.append(lesson)
            schedule.append(exercise)
        elif lesson in schedule and exercise not in schedule:  # If the lesson exists and there is no exercise add
            # Exercise in the schedule right after the lesson index
            schedule.insert(schedule.index(lesson) + 1, exercise)

    command = input().split(":")

# Output
for element in schedule:
    print(f"{schedule.index(element) + 1}.{element}")
