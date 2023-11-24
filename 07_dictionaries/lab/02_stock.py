# Create a dictionary of the user's input
key_values = input().split()
searched_products = input().split()

inventory = {}

# Search for each item in the user's input
for i in range(0, len(key_values), 2):
    item = key_values[i]
    quantity = int(key_values[i + 1])
    inventory[item] = quantity

for current_searched_product in searched_products:
    if current_searched_product in inventory.keys():
        print(f"We have {inventory.get(current_searched_product)} of {current_searched_product} left")
    else:
        print(f"Sorry, we don't have {current_searched_product}")
