import re

text_to_search = input()
word_to_search = input()

regex = fr"\b{word_to_search}\b"

matches = re.findall(regex, text_to_search, re.IGNORECASE)
occurrences = len(matches)

print(occurrences)
