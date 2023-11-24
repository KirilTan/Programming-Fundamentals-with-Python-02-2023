inventory = {}

while True:
    user_input = input()

    if user_input == "statistics":
        break
    else:
        product, quantity = user_input.split(": ")
        quantity = int(quantity)

    if product in inventory:
        inventory[product] += quantity
    else:
        inventory[product] = quantity

product_count = len(inventory.keys())
total_quantity = sum(inventory.values())

# Output
print("Products in stock:")
for product, quantity in inventory.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {product_count}")
print(f"Total Quantity: {total_quantity}")
