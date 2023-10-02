# Input
budget = float(input())
flour_price_per_kg = float(input())

# Prices and quantities
egg_price_per_kg_flour = 0.75 * flour_price_per_kg
milk_price_per_kg_flour = 1.25 * flour_price_per_kg
milk_quantity_per_bread = 0.25  # in liters

# Initializations
loaves = 0
colored_eggs = 0

# Cooking loaves until the budget allows
while budget >= flour_price_per_kg:
    budget -= flour_price_per_kg
    budget -= egg_price_per_kg_flour
    budget -= milk_price_per_kg_flour * milk_quantity_per_bread

    loaves += 1
    colored_eggs += 3

    # Losing eggs on every 3rd bread
    if loaves % 3 == 0:
        lost_eggs = loaves - 2
        colored_eggs -= lost_eggs

# Output
money_left = format(budget, '.2f')
print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left}BGN left.")
