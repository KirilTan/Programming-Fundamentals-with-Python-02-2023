code_word = input()
word_to_decode = input()

new_word = str(word_to_decode)
while code_word in new_word:
    new_word = new_word.replace(code_word, "")

print(new_word)
