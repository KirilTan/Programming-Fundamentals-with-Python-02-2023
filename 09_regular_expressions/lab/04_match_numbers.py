import re

regex = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

test_str = input()

matches = re.finditer(regex, test_str)

for match in matches:
    print(match.group(), end=" ")
