start_range = int(input())
end_range = int(input())

for number in range(start_range, end_range + 1):
    character = chr(number)
    print(character, end=" ")

