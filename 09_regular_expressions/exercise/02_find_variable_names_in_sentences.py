import re

user_input = input()

regex = r"\b_([A-Za-z0-9]+)\b"
matches = re.findall(regex, user_input)

print(",".join(matches))
