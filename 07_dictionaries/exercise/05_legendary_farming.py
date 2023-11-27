inventory = {
    "shards": 0,
    "fragments": 0,
    "motes": 0,
}

item_won = ""
game_over = False
while not game_over:
    # Input
    user_input = input().lower().split()

    # Logic
    for index in range(0, len(user_input), 2):
        current_item = user_input[index + 1]
        current_item_amount = user_input[index]

        key = current_item
        value = current_item_amount

        if key not in inventory.keys():
            inventory[key] = 0
        inventory[key] += int(value)

        if inventory["shards"] >= 250:
            inventory["shards"] -= 250
            item_won = "Shadowmourne"
            game_over = True
        elif inventory["fragments"] >= 250:
            item_won = "Valanyr"
            game_over = True
            inventory["fragments"] -= 250
        elif inventory["motes"] >= 250:
            item_won = "Dragonwrath"
            inventory["motes"] -= 250
            game_over = True

        if game_over:
            break
    if game_over:
        break

# Output
print(f"{item_won} obtained!")
for material, amount in inventory.items():
    print(f"{material}: {amount}")

