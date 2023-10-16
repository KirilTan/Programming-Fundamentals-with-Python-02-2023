def calculations(operator: str, num1: int, num2: int):
    if operator == "multiply":
        return num1 * num2
    elif operator == "divide":
        return int(num1 / num2)
    elif operator == "add":
        return num1 + num2
    elif operator == "subtract":
        return num1 - num2
    else:
        return "Operator not supported"


operator = input()
num1 = int(input())
num2 = int(input())
print(calculations(operator=operator, num1=num1, num2=num2))
