input_list = input().split()

command = input().split()
while not command[0] == "3:1":

    if command[0] == "merge":  # Merge elements from the start_index to the end index_index
        start_index, end_index = int(command[1]), int(command[2])

        #  If any of the given indexes is out of the array, take only the range that is inside the array and merge it.
        if start_index < 0:
            start_index = 0
        if end_index > len(input_list) - 1:
            end_index = len(input_list) - 1

        # Merging elements from start_index to end_index index
        merged_elements = "".join(input_list[start_index:end_index + 1])
        input_list[start_index:end_index + 1] = [merged_elements]

    elif command[0] == "divide":
        # Divide the element at the given index into several small substrings with equal length.
        # The count of the substrings should be equal to the given partitions
        index, partitions = int(command[1]), int(command[2])

        if partitions > len(input_list[index]):
            step = 1
        else:
            step = len(input_list[index]) // partitions

        part_to_divide = input_list.pop(index)
        start = 0

        for parts in range(partitions):

            if parts == partitions - 1:
                input_list.insert(index, part_to_divide[start::])
                break
            else:
                input_list.insert(index, part_to_divide[start: start + step:])

            start += step
            index += 1

    command = input().split()
print(" ".join(input_list))