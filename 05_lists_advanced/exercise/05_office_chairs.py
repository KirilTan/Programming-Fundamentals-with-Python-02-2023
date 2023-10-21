number_of_inputs = int(input())

free_chairs = 0
everything_ok = True
for current_room in range(number_of_inputs):

    current_operation = input().split()
    chairs = len(current_operation[0])
    visitors = int(current_operation[1])

    if visitors <= chairs:
        free_chairs += abs(visitors - chairs)
        continue
    else:
        print(f"{abs(visitors - chairs)} more chairs needed in room {current_room + 1}")
        everything_ok = False

if everything_ok:
    print(f"Game On, {free_chairs} free chairs left")
