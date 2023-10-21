number_of_electrons = int(input())
shells = []

current_shell = 0
while number_of_electrons:
    current_shell += 1
    max_input = 2 * (current_shell**2)
    current_input = 0

    if max_input <= number_of_electrons:
        number_of_electrons -= max_input
        current_input = max_input
        shells.append(current_input)
    else:
        current_input = number_of_electrons
        shells.append(current_input)
        break

print(shells)
