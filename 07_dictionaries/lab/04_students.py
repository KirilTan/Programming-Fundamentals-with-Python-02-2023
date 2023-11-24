students = []
searched_course = None

while True:

    student_info = input()

    if ":" not in student_info:
        searched_course = student_info
        break

    name, ID, course = student_info.split(":")
    students.append({"name": name,"ID": ID,"course": course})

for current_student in students:
    if searched_course.startswith(current_student["course"][0:3]):
        print(f"{current_student['name']} - {current_student['ID']}")
