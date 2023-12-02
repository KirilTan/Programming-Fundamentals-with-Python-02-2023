# Initial input and collecting info

info = {
    "Cities": [],
    "Population": [],
    "Gold": []
}

command = input()
while command != "Sail":

    city, population, gold = command.split("||")

    if city not in info["Cities"]:
        info["Cities"].append(city)
        info["Population"].append(int(population))
        info["Gold"].append(int(gold))
    else:
        index = info["Cities"].index(city)
        info["Population"][index] += int(population)
        info["Gold"][index] += int(gold)

    command = input()

# Actions

command = input()
gold_stolen = 0
people_killed = 0
while command != "End":

    command = command.split("=>")

    if command[0] == "Plunder":

        town, people, gold = command[1], int(command[2]), int(command[3])

        if town in info["Cities"]:
            index = info["Cities"].index(town)
            info["Population"][index] -= people
            info["Gold"][index] -= gold
            people_killed += people
            gold_stolen += gold
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

            if info["Gold"][index] <= 0 or info["Population"][index] <= 0:
                # Remove town from list
                info["Cities"].remove(town)
                del info["Population"][index]
                del info["Gold"][index]
                print(f"{town} has been wiped off the map!")

        else:  # town not in info["Cities"]:
            command = input()
            continue

    elif command[0] == "Prosper":

        town, gold = command[1], int(command[2])

        if town in info["Cities"] and gold >= 0:
            index = info["Cities"].index(town)
            info["Gold"][index] += gold
            total_town_gold = info["Gold"][index]
            print(f"{gold} gold added to the city treasury. {town} now has {total_town_gold} gold.")

        elif town in info["Cities"] and gold < 0:
            print(f"Gold added cannot be a negative number!")
            command = input()
            continue

        else:  # town not in info["Cities"]:
            command = input()
            continue

    command = input()

# Output after "End" command

if len(info["Cities"]) > 0:
    remaining_cities = len(info["Cities"])
    print(f"Ahoy, Captain! There are {remaining_cities} wealthy settlements to go to:")

    for city, population, gold in zip(info["Cities"], info["Population"], info["Gold"]):
        print(f"{city} -> Population: {population} citizens, Gold: {gold} kg")

else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
