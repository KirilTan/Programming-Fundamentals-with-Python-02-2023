# Inputs
group_size = int(input())
days = int(input())

# Calculations
coins = 0
for current_day in range(1, days + 1):

    if current_day % 10 == 0:
        group_size -= 2
    if current_day % 15 == 0:
        group_size += 5

    coins += 50              # Daily coin gain
    coins -= group_size * 2  # Daily rations

    if current_day % 3 == 0:
        coins -= group_size * 3     # Water rations
    if current_day % 5 == 0:
        coins += group_size * 20    # Boss slain reward
        if current_day % 3 == 0:
            coins -= group_size * 2
coins_per_person = coins // group_size

# Output
print(f"{group_size} companions received {coins_per_person} coins each.")
