# Function to get the average of a list
def average(numbers_list: list) -> float:

    """This function takes a list of numbers and returns the average of the numbers."""

    return sum(numbers_list) / len(numbers_list)


# Inputs
employee_happiness_list = [int(number) for number in input().split()]
happiness_improvement_factor = int(input())

# Logic
employee_happiness_after_improvement_factor = [int(employee_happiness * happiness_improvement_factor) for employee_happiness in employee_happiness_list]
average_happiness = average(employee_happiness_after_improvement_factor)

happy_employees = [int(s) for s in employee_happiness_after_improvement_factor if s >= average_happiness]
amount_of_happy_employees = len(happy_employees)
total_employees = len(employee_happiness_list)

# Output
if amount_of_happy_employees >= (total_employees / 2):
    print(f"Score: {amount_of_happy_employees}/{total_employees}. Employees are happy!")
else:
    print(f"Score: {amount_of_happy_employees}/{total_employees}. Employees are not happy!")
