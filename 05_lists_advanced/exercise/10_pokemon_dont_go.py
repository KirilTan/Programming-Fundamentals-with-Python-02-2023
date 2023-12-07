input_list = [int(item) for item in input().split()]

score = 0
while input_list:  # The program ends when the sequence has no elements

    # When you receive an index, you must remove the element at that index from the sequence
    index = int(input())
    if index < 0:  # If the given index is less than 0 remove the first element of the sequence and copy the last
        # element to its place
        caught_pokemon = input_list[0]
        input_list[0] = input_list[-1]
    elif index > len(input_list) - 1:  # If the given index is greater than the last index of the sequence, remove
        # the last element from the sequence, and copy the first element to its place
        caught_pokemon = input_list[-1]
        input_list[-1] = input_list[0]
    else:
        caught_pokemon = input_list.pop(index)

    for current_index in range(len(input_list)):  # Increase or decrease the value of all elements in the sequence
        # based on the value of the removed element
        if input_list[current_index] <= caught_pokemon:
            input_list[current_index] += caught_pokemon
        else:
            input_list[current_index] -= caught_pokemon

    score += int(caught_pokemon)

print(score)