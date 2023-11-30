import re

regex = r"(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})"

test_str = input()

matches = re.findall(regex, test_str)

for match in matches:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")
