number_of_inputs = int(input())

database = {}
for _ in range(number_of_inputs):

    current_student_name = input()
    current_student_grade = float(input())

    if current_student_name not in database.keys():
        database[current_student_name] = []
    database[current_student_name].append(current_student_grade)

for student, grades in database.items():
    average_grade = sum(grades) / len(grades)

    if average_grade >= 4.5:
        print(f"{student} -> {average_grade:.2f}")
