number_of_inputs = int(input())

for _ in range(number_of_inputs):

    current_number = int(input())

    if current_number % 2 != 0:
        print(f'{current_number} is odd!')
        break

else:
    print(f'All numbers are even.')
