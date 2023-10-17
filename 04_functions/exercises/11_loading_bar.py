def loading_bar(number: int) -> str:
    if number == 100:
        return ("100% Complete!\n"
                "[%%%%%%%%%%]")
    else:
        x = number // 10
        return (f"{number}% [{x * '%'}{(10 - x) * '.'}]\n"
                f"Still loading...")


input_number = int(input())
print(loading_bar(input_number))
