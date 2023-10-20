def data_types(value_type: str, value: int or str or float) -> int or float or str:

    if value_type == "string":
        new_value = f"${value}$"
    elif value_type == "int":
        new_value = int(value) * 2
    elif value_type == "real":
        new_value = float(value) * 1.5
        new_value = f"{new_value:.2f}"
    else:
        new_value = "Invalid value type"

    return new_value


input_value_type = input()
input_value = input()
print(data_types(value_type=input_value_type, value=input_value))
