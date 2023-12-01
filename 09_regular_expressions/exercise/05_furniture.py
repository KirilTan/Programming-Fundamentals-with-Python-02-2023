import re

shopping_cart = {"Furniture": [], "Price": [], "Quantity": []}
user_input = input()
while user_input != "Purchase":

    regex = r">>([A-Za-z]+)<<([0-9]+\.?\d*)!([0-9]+)"
    matches = re.search(regex, user_input)

    if matches:
        furniture_type, price, qty = matches.groups()
        shopping_cart["Furniture"].append(furniture_type)
        shopping_cart["Price"].append(price)
        shopping_cart["Quantity"].append(qty)

    user_input = input()

total_money_spent = 0
for price, qty in zip(shopping_cart["Price"], shopping_cart["Quantity"]):
    total_money_spent += float(price) * int(qty)

print("Bought furniture:")
for furniture in shopping_cart["Furniture"]:
    print(furniture)
print("Total money spend: {:.2f}".format(total_money_spent))
