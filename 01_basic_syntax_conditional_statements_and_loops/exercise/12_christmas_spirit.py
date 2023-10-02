# Input
quantity_of_decorations = int(input())
days_to_christmas = int(input())

# Price
total_price = 0
ornament_price = 2
skirt_price = 5
garland_price = 3
lights_price = 15

# Spirit
total_spirit = 0
ornament_spirit = 5
skirt_spirit = 3
garland_spirit = 10
lights_spirit = 17

# Calculations
for current_day in range(1, days_to_christmas + 1):
    if current_day % 11 == 0:
        quantity_of_decorations += 2
    if current_day % 2 == 0:
        total_price += ornament_price * quantity_of_decorations
        total_spirit += ornament_spirit
    if current_day % 3 == 0:
        total_price += (skirt_price + garland_price) * quantity_of_decorations
        total_spirit += skirt_spirit + garland_spirit
    if current_day % 5 == 0:
        total_price += lights_price * quantity_of_decorations
        total_spirit += lights_spirit
        if current_day % 3 == 0:
            total_spirit += 30
    if current_day % 10 == 0:
        total_price += skirt_price + garland_price + lights_price
        total_spirit -= 20

if days_to_christmas % 10 == 0:
    total_spirit -= 30

# Output
print(f"Total cost: {total_price}")
print(f"Total spirit: {total_spirit}")
