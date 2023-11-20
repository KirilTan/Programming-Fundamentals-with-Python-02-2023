class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        return_string = ""

        if species == "mammal":
            return_string += f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}"
        elif species == "fish":
            return_string += f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}"
        elif species == "bird":
            return_string += f"Birds in {self.zoo_name}: {', '.join(self.birds)}"

        return_string += (f"\n"
                          f"Total animals: {Zoo.__animals}")

        return return_string


# Inputs
name_of_zoo = input()
zoo_instance = Zoo(name_of_zoo)

number_of_inputs = int(input())
for current_input in range(number_of_inputs):

    # Add animal to species
    current_animal_species, current_animal_name = input().split()
    zoo_instance.add_animal(current_animal_species, current_animal_name)

# Output
species_for_output = input()
print(zoo_instance.get_info(species_for_output))
