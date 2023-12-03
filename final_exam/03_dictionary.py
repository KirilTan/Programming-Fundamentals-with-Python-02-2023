dictionary = {}

word_and_definition = input().split("|")
for current_word_and_definition in word_and_definition:

    word, definition = current_word_and_definition.split(":")
    word = word.strip()

    if word not in dictionary:
        dictionary[word] = [definition]
    else:  # Add the definition to the existing dictionary
        dictionary[word].append(definition)

test_words = input().split("|")
command = input()

if command == "Hand Over":  # Print only the words(without the definitions)
    for current_word in dictionary.keys():
        print(current_word, end=" ")

elif command == "Test":  # Print all the definitions for the test words
    for current_word in test_words:
        current_word = current_word.strip()
        if current_word in dictionary.keys():
            print(f"{current_word}:")
            for definition in dictionary[current_word]:
                print(f" -{definition.strip()}")