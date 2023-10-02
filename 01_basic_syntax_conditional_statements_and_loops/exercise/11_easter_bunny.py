# Inputs
budget = float(input())
flour_price_per_kg = float(input())

# Prices
eggs_price_per_pack = .75 * flour_price_per_kg
milk_price_per_l = 1.25 * flour_price_per_kg

# Recipe
loaf_price_per_unit = (1 * eggs_price_per_pack) + (1 * flour_price_per_kg) + (.25 * milk_price_per_l)

#
colored_eggs_count = 0
money_left = budget
current_loaf = 0

while True:

    if money_left - loaf_price_per_unit > 0:
        money_left -= loaf_price_per_unit
    else:
        break

    current_loaf += 1
    colored_eggs_count += 3

    if current_loaf % 3 == 0:
        eggs_lost = current_loaf - 2
        colored_eggs_count -= eggs_lost



print(f"You made {current_loaf} loaves of Easter bread! "
      f"Now you have {colored_eggs_count} eggs and {money_left:.2f}BGN left.")