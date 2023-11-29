# def emoticon_finder(text: str) -> list:
#     """
#     This function returns the emoticons in a given text.
#     Emoticons always start with ":" and are followed by a symbol.
#     """
#
#     emoticons = []
#
#     sentences = text.split(".")
#     words = []
#     for sentence in sentences:
#         sentence_words = sentence.split(" ")
#         words.extend(sentence_words)
#
#     for word in words:
#         if word.startswith(":"):
#             emoticons.append(word)
#
#     return emoticons
#
#
# input_text = input()
#
# emoticons_list = emoticon_finder(input_text)
#
# for emoticon in emoticons_list:
#     print(emoticon)


input_string = input()
for index in range(len(input_string)):
    if input_string[index] == ":":
        print(f":{input_string[index + 1]}")