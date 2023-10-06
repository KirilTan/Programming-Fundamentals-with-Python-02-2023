# Inputs and constants
number_of_inputs = int(input())
capacity = 255  # In liters

# Calculations
capacity_left = capacity
water_poured = 0
for line in range(number_of_inputs):
    current_input = int(input())
    if capacity_left - current_input >= 0:
        capacity_left -= current_input
        water_poured += current_input
    else:
        print("Insufficient capacity!")

# Output
print(water_poured)
