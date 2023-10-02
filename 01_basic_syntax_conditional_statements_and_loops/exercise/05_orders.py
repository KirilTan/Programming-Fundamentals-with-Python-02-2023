number_of_orders = int(input())

total_price = 0

for _ in range(number_of_orders):

    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())

    if not 0.01 <= price_per_capsule <= 100:
        continue

    if not 1 <= days <= 31:
        continue

    if not 1 <= capsules_needed_per_day <= 2000:
        continue

    current_price = price_per_capsule * days * capsules_needed_per_day
    total_price += current_price
    print(f"The price for the coffee is: ${current_price:.2f}")

print(f"Total: ${total_price:.2f}")
