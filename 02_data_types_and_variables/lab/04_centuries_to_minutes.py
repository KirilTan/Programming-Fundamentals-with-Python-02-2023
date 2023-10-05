# Input
centuries = int(input())

# Calculations
years = centuries * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60

text_for_print = (f"{centuries} centuries = "
                  f"{years} years = "
                  f"{days} days = "
                  f"{hours} hours = "
                  f"{minutes} minutes")

# Output
print(text_for_print)
