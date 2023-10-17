from math import factorial

num1 = int(input())
num2 = int(input())

num1_factorial = factorial(num1)
num2_factorial = factorial(num2)

result = num1_factorial / num2_factorial

print(f"{result:.2f}")
