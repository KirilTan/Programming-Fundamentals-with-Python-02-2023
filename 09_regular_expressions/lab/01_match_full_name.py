import re

regex = "\\b[A-Z][a-z]+ [A-Z][a-z]+\\b"

test_str = input()

matches = re.findall(regex, test_str)

print(" ".join(matches))
