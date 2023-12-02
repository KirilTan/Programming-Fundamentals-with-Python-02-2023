# Initial data collection
cars_info = {
    "Car": [],
    "Mileage": [],
    "Fuel": []
}

number_of_inputs = int(input())

for _ in range(number_of_inputs):
    car, mileage, fuel = input().split("|")

    cars_info["Car"].append(car)
    cars_info["Mileage"].append(int(mileage))
    cars_info["Fuel"].append(int(fuel))

# Actions

command = input().split(":")
while command[0] != "Stop":

    if command[0].strip() == "Drive":
        car, distance, fuel = command[1].strip(), int(command[2]), int(command[3])
        index = cars_info["Car"].index(car)

        if cars_info["Fuel"][index] >= fuel:   # If the car has the required fuel available in the tank
            cars_info["Mileage"][index] += distance  # Increase the mileage of the car
            cars_info["Fuel"][index] -= fuel  # Reduce the fuel of the car
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        else:  # Not enough fuel to make that ride
            print(f"Not enough fuel to make that ride")

        if cars_info["Mileage"][index] >= 100_000:  # If a car's mileage reaches 100000 km, remove it from the collection

            print(f"Time to sell the {car}!")

            cars_info["Car"].remove(car)
            del cars_info["Mileage"][index]
            del cars_info["Fuel"][index]

    elif command[0].strip() == "Refuel":

        car, fuel = command[1].strip(), int(command[2])
        index = cars_info["Car"].index(car)
        maximum_fuel = 75

        starting_fuel = cars_info["Fuel"][index]

        if cars_info["Fuel"][index] + fuel <= maximum_fuel:
            cars_info["Fuel"][index] += fuel
        else:
            cars_info["Fuel"][index] = maximum_fuel

        refueled_fuel = cars_info["Fuel"][index] - starting_fuel
        print(f"{car} refueled with {refueled_fuel} liters")

    elif command[0].strip() == "Revert":  # Decrease the mileage of the given car with the given amount of kilometers
        car, kilometers = command[1].strip(), int(command[2])
        index = cars_info["Car"].index(car)

        # If the mileage becomes less than 10 000km after it is decreased, set it to 10 000km
        if cars_info["Mileage"][index] - kilometers >= 10_000:
            cars_info["Mileage"][index] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")
        else:
            cars_info["Mileage"][index] = 100000

    command = input().split(":")

# Output
for car, mileage, fuel in zip(cars_info["Car"], cars_info["Mileage"], cars_info["Fuel"]):
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")
