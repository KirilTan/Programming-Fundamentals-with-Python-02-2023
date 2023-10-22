number_of_cities = int(input())

total_profit = 0.00
for current_city in range(1, number_of_cities + 1):

    city_name = input()
    current_income = float(input())
    current_cost = float(input())

    if current_city % 5 == 0:  # lose 10% of money earned
        current_income *= 0.9
    elif current_city % 3 == 0:  # Additional 50% over costs
        current_cost *= 1.5

    current_profit = current_income - current_cost
    total_profit += current_profit

    print(f"In {city_name} Burger Bus earned {current_profit:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")
