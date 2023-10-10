starting_deck = input().split(" ")
number_of_shuffles = int(input())

middle_of_starting_deck = len(starting_deck) // 2

for current_shuffle in range(number_of_shuffles):

    left_part = starting_deck[:middle_of_starting_deck]
    right_part = starting_deck[middle_of_starting_deck:]

    shuffled_deck = []

    for current_card in range(len(left_part)):  # left_part == right_part
        shuffled_deck.append(left_part[current_card])
        shuffled_deck.append(right_part[current_card])

    starting_deck = shuffled_deck

print(shuffled_deck)
