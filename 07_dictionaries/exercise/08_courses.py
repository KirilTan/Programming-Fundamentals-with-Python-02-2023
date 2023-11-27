courses_students = {}

command = input()
while command != "end":

    course_name, student_name = command.split(" : ")

    if course_name not in courses_students.keys():
        courses_students[course_name] = []
    courses_students[course_name].append(student_name)

    command = input()

for course_name, students in courses_students.items():
    print(f"{course_name}: {(len(students))}")
    for student in students:
        print(f"-- {student}")
