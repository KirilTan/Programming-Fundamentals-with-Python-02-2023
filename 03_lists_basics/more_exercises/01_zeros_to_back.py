list_of_numbers = input().split(", ")

number_of_zeros = list_of_numbers.count("0")

for _ in range(number_of_zeros):
    list_of_numbers.remove("0")
    list_of_numbers.append("0")

print("[" +
      ", ".join(list_of_numbers)
      + "]")
