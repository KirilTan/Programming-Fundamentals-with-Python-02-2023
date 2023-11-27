command = input()

database = {}
while command != "End":

    employer, employee = command.split(" -> ")

    if employer not in database.keys():
        database[employer] = []

    if employee in database[employer]:
        command = input()
        continue

    database[employer].append(employee)

    command = input()

for employer, employees in database.items():
    print(employer)
    for employee in employees:
        print(f"-- {employee}")
