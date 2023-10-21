def sum_numbers(a: int, b: int) -> int:
    return a + b


def subtract(result: int, c: int) -> int:
    return result - c


def add_and_subtract(a: int, b: int, c: int) -> int:
    sum_of_a_b = sum_numbers(a, b)
    subtract_result = subtract(sum_of_a_b, c)
    return subtract_result


num1 = int(input())
num2 = int(input())
num3 = int(input())
print(add_and_subtract(num1, num2, num3))
