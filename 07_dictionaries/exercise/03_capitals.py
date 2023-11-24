# User input
countries = input().split(", ")
capitals = input().split(", ")

# Creating a dictionary
country_capital_dict = {country: capital for country, capital in zip(countries, capitals)}

# Output
for country, capital in country_capital_dict.items():
    print(f"{country} -> {capital}")
