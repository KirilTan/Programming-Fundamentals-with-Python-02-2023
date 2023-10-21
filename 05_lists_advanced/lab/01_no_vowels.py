input_str = input()
vowels_to_be_removed = ['a', 'o', 'u', 'e', 'i']
new_list = [char for char in input_str if char.lower() not in vowels_to_be_removed]
print(*new_list, sep="")
