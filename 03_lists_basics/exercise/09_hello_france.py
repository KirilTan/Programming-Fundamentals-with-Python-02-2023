# Input
collection_of_items = input().split('|')
budget = float(input())
price_of_items_bought = []

# Calculations
for i in collection_of_items:
    item_name, item_price = i.split('->')
    item_price = float(item_price)
    valid = False

    if item_name == 'Clothes' and item_price <= 50:
        valid = True
    elif item_name == 'Shoes' and item_price <= 35:
        valid = True
    elif item_name == 'Accessories' and item_price <= 20.50:
        valid = True

    if valid:
        if budget - item_price < 0:
            break

        budget -= item_price
        price_of_items_bought.append(item_price)

items_with_profit = [item * 1.4 for item in price_of_items_bought]

# Output
for item in items_with_profit:
    print(f'{item:.2f}', end=' ')

print()
print(f'Profit: {abs(sum(price_of_items_bought) - sum(items_with_profit)):.2f}')
if sum(items_with_profit) + budget >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
