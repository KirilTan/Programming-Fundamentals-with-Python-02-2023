# Inputs
total_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

# Calculations
helmet_broken_times = total_lost_fights // 2
sword_broken_times = total_lost_fights // 3
shield_broken_times = total_lost_fights // 6
armor_broken_times = shield_broken_times // 2

helmet_expenses = helmet_broken_times * helmet_price
sword_expenses = sword_broken_times * sword_price
shield_expenses = shield_broken_times * shield_price
armor_expenses = armor_broken_times * armor_price

total_expenses = helmet_expenses + sword_expenses + shield_expenses + armor_expenses

# Output
print(f"Gladiator expenses: {total_expenses:.2f} aureus")
