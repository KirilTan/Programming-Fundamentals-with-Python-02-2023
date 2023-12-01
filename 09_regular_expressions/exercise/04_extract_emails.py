import re


user_input = input()
regex = r" \b([a-z0-9]+[a-z0-9\.\-\_]*@[a-z\-]+([.][a-z]+)+)\b"
matches = re.findall(regex, user_input)

for match in matches:
    print(match[0])