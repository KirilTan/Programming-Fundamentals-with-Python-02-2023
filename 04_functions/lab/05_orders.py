# Prices
coffee_price = 1.50
water_price = 1.00
coke_price = 1.40
snacks_price = 2.00


def get_total_price(product: str, quantity: int):
    if product == "coffee":
        return f"{(coffee_price * quantity):.2f}"
    elif product == "water":
        return f"{(water_price * quantity):.2f}"
    elif product == "coke":
        return f"{(coke_price * quantity):.2f}"
    elif product == "snacks":
        return f"{(snacks_price * quantity):.2f}"
    else:
        return "Invalid input"


product_type = input()
amount = int(input())


print(get_total_price(product_type, amount))
