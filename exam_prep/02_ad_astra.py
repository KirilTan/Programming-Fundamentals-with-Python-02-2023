import re

# Input and input formatting
input_string = input()

regex = r"(?i)(\||#)([a-z\s]+)(\1)(\d{2}\/\d{2}\/\d{2})(\1)(\d+)(\1)"
matches = re.findall(regex, input_string)  # Index 1 - item_name, Index 3 - expiration_date, Index 5 - calories

inventory = {
    "Item names": [],
    "Expiration dates": [],
    "Calories": []
}

for match in matches:
    inventory["Item names"].append(match[1])
    inventory["Expiration dates"].append(match[3])
    inventory["Calories"].append(int(match[5]))

# Logic and output
calories_per_day = 2000
total_calories_from_food = sum(inventory["Calories"])
days_worth_of_food = int(total_calories_from_food / calories_per_day)

if days_worth_of_food <= 0:
    print("You have food to last you for: 0 days!")
else:
    print(f"You have food to last you for: {days_worth_of_food} days!")
    for item_name, expiration_date, calories in zip(inventory["Item names"],
                                                    inventory["Expiration dates"],
                                                    inventory["Calories"]):

        print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")
