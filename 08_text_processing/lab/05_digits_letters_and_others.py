# user_input = input()
#
# digits = ""
# letters = ""
# other_characters = ""
#
# for character in user_input:
#     if character.isdigit():
#         digits += character
#     elif character.isalpha():
#         letters += character
#     else:
#         other_characters += character
#
# print(digits)
# print(letters)
# print(other_characters)

user_input = input()

text_composition = {
    "digits": "",
    "letters": "",
    "other_characters": ""
}

for character in user_input:
    if character.isdigit():
        text_composition["digits"] += character
    elif character.isalpha():
        text_composition["letters"] += character
    else:
        text_composition["other_characters"] += character

for key, value in text_composition.items():
    print(f"{key.capitalize()}: {value}")
