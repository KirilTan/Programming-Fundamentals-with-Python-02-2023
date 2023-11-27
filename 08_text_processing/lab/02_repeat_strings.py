input_text = input().split()

new_text = ""
for word in input_text:
    new_text += word * (len(word))

print(new_text)

# print(*[text * len(text) for text in input().split()], sep="")
