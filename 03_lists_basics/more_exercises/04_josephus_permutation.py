circle = input().split()
step = int(input())
execution_order = []

index = 0
while circle:
    index = (index + step - 1) % len(circle)
    execution_order.append(circle.pop(index))

print("[" + ",".join(execution_order) + "]")

