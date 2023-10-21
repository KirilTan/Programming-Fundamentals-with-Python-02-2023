# Function to get the average of a list
def average(numbers_list: list) -> float:

    """This function takes a list of numbers and returns the average of the numbers."""

    return sum(numbers_list) / len(numbers_list)


# Function to get the amount of happy employees in a list
def amount_of_happy_employees(employee_scores: list, factor: int) -> int:
    """This function takes a list of numbers and returns the amount of happy employees in the list.
    Happy employees are employees who have a score greater than the average of the employees' scores after improvement
    factor is applied."""

    employee_scores_after_improvement_factor = list(map(lambda x: x * factor, employee_scores))
    average_score = average(employee_scores_after_improvement_factor)
    happy_employees = list(filter(lambda x: x >= average_score, employee_scores_after_improvement_factor))
    return len(happy_employees)


# Inputs
employee_happiness_list = [int(number) for number in input().split()]
happiness_improvement_factor = int(input())

# Variables
total_employees = len(employee_happiness_list)
happy_employees_count = amount_of_happy_employees(employee_happiness_list, happiness_improvement_factor)

# Output
if happy_employees_count >= (total_employees / 2):
    print(f"Score: {happy_employees_count}/{total_employees}. Employees are happy!")
else:
    print(f"Score: {happy_employees_count}/{total_employees}. Employees are not happy!")
