banned_words = input().split(", ")
text = input()

new_text = str(text)

for word in banned_words:
    while word in new_text:
        new_text = new_text.replace(word, ("*" * len(word)))

print(new_text)
