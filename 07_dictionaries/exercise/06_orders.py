shopping_cart = {}

user_input = input()

while user_input != "buy":

    current_item, current_item_price, current_item_quantity = user_input.split()
    current_item_quantity = int(current_item_quantity)
    current_item_price = float(current_item_price)

    if current_item in shopping_cart:
        price_in_cart = shopping_cart[current_item][0][-1]
        quantity_in_cart = shopping_cart[current_item][0][1]
        new_quantity = quantity_in_cart + current_item_quantity
        shopping_cart[current_item][-1] = [current_item_price, new_quantity]
    else:
        shopping_cart[current_item] = [[current_item_price, current_item_quantity]]

    user_input = input()

for key, value in shopping_cart.items():

    current_item_price = value[0][0]
    current_item_quantity = value[0][1]
    total_price = f"{(current_item_price * current_item_quantity):.2f}"

    print(f"{key} -> {total_price}")
