# Input
year = int(input())

# Calculations
while True:

    year += 1
    year_as_string = str(year)

    if len(year_as_string) == len(set(year_as_string)):
        break

# Output
print(year)