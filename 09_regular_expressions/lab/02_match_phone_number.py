import re

regex = "\\+359-2{1}-\d{3}-\d{4}\\b|\+359 2{1} \d{3} \d{4}\\b"

test_str = input()

matches = re.findall(regex, test_str)

print(", ".join(matches))
