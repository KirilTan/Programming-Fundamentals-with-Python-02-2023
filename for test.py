# Input
num1 = int(input())
num2 = int(input())

# Print before swapping
print(f"Before:\n"
      f"a = {num1}\n"
      f"b = {num2}")

# Swapping values using tuple unpacking
num1, num2 = num2, num1

# Print after swapping
print(f"After:\n"
      f"a = {num1}\n"
      f"b = {num2}")
