command = input()

total_coffee_needed = 0

while command != "END":

    current_activity = command

    if current_activity.lower() == "coding" \
            or current_activity.lower() == "dog"\
            or current_activity.lower() == "cat" \
            or current_activity.lower() == "movie":
        if current_activity.islower():
            total_coffee_needed += 1
        elif current_activity.isupper():
            total_coffee_needed += 2

    command = input()

if total_coffee_needed > 5:
    print("You need extra sleep")
else:
    print(total_coffee_needed)
