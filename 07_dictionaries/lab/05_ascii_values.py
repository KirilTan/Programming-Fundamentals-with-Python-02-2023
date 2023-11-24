user_input = input().split(", ")

output = {letter: ord(letter) for letter in user_input}

print(output)
