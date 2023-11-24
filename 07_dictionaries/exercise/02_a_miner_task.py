inventory = {}
while True:

    resource = input()
    if resource == "stop":
        break
    quantity = int(input())

    if resource not in inventory:
        inventory[resource] = quantity
    else:
        inventory[resource] += quantity

# Output
for current_resource, current_quantity in inventory.items():
    print(f"{current_resource} -> {current_quantity}")
