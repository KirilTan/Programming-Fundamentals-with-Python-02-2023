user_input = input().split()

inventory = {}

for i in range(0, len(user_input), 2):
    item = user_input[i]
    quantity = int(user_input[i + 1])
    inventory[item] = quantity

print(inventory)
