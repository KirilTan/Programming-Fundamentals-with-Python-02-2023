user_input = input()

results = {}
submissions = {}

while user_input != "exam finished":

    command = user_input.split("-")
    name = command[0]

    # Results logic
    if command[1] != "banned":
        subject = command[1]
        result = int(command[2])

        # If the user is not present in the list of results, add him with the current result
        if name not in results:
            results[name] = result
        else:
            # If the user is present, update the result only if the current result is higher
            results[name] = max(results[name], result)

        # Submissions logic
        if subject not in submissions:
            submissions[subject] = 0
        submissions[subject] += 1

    # Ban logic
    elif command[1] == "banned":
        # Remove the user from results, but keep the submissions
        results.pop(name, None)

    user_input = input()

# Output
print("Results:")
for name, result in results.items():
    if result is not None:
        print(f"{name} | {result}")

print("Submissions:")
for subject, count in submissions.items():
    print(f"{subject} - {count}")
