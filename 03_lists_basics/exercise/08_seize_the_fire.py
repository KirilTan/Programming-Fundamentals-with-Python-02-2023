# Inputs
fire_level = input().split("#")
total_water = int(input())

# Calculations
situations_resolved = []
total_effort = 0
for current_situation in fire_level:
    type_of_fire, value_of_cell = current_situation.split(" = ")
    value_of_cell = int(value_of_cell)
    valid = False

    if type_of_fire == "High" and 81 <= value_of_cell <= 125 and value_of_cell <= total_water:
        valid = True
    elif type_of_fire == "Medium" and 51 <= value_of_cell <= 80 and value_of_cell <= total_water:
        valid = True
    elif type_of_fire == "Low" and 1 <= value_of_cell <= 50 and value_of_cell <= total_water:
        valid = True

    if valid:
        situations_resolved.append(value_of_cell)
        total_water -= value_of_cell
        total_effort += 0.25 * value_of_cell

# Output
print("Cells:")
for situation in situations_resolved:
    print(f" - {situation}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {sum(situations_resolved)}")
