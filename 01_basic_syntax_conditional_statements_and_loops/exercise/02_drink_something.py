age = int(input())
beverage = ""

if age <= 14:
    beverage = "toddy"
elif age <= 18:
    beverage = "coke"
elif age <= 21:
    beverage = "beer"
else:
    beverage = "whisky"

print(f"drink {beverage}")
