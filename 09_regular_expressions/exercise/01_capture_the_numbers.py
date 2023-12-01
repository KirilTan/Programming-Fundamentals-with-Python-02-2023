import re

user_input = input()

while user_input:
    regex = r"\d+"
    matches = re.findall(regex, user_input, )

    if matches:
        print(" ".join(matches), end=" ")

    user_input = input()
