# Passwords for contest
user_input = input()

passwords_for_contests = {}

while user_input != "end of contests":
    contest_name, contest_password = user_input.split(":")
    passwords_for_contests[contest_name] = contest_password
    user_input = input()

# Contestants information
user_input = input()

scores = {}

while user_input != "end of submissions":
    contest_name, contest_password, username, score = user_input.split("=>")

    # Check if contest exists and password is correct
    if contest_name in passwords_for_contests and contest_password == passwords_for_contests[contest_name]:
        # Check if old score exists and if new score is greater than old score
        if username in scores and score > max(scores[username], key=lambda x: x[1])[1]:
            scores[username].append([contest_name, score])
        # If no old score exists, add new score
        else:
            scores[username] = [[contest_name, score]]

    user_input = input()

# Output
total_scores = {}

for username, user_scores in scores.items():
    for contest_name, score in user_scores:
        if contest_name not in total_scores:
            total_scores[contest_name] = {}
        total_scores[contest_name][username] = score

# Find the best candidate
best_candidate = max(scores.keys(), key=lambda x: sum(int(score[1]) for score in scores[x]))

print(f"Best candidate is {best_candidate} with total {sum(int(score[1]) for score in scores[best_candidate])} points.")

# Print all students ordered by their names
for username in sorted(scores.keys()):
    print(username)
    for contest_name, score in sorted(total_scores.items(), key=lambda x: x[0]):
        if username in score:
            print(f"#  {contest_name} -> {score[username]}")
