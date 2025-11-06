from data_input import input_employees
from salary_calc import calculate_salary, add_bonus


def print_employees_recursive(names, index=0):
    if index < len(names):  #якщо індекс дорівнює довжині списку, це означає імена закінчились та рекурсія закінчилась
        print(names[index])
        print_employees_recursive(names, index + 1)


def main():
    employees = input_employees()

    print("\n Розрахунок зарплат: ")
    for name, data in employees.items():
        base_salary = calculate_salary(data["salary"], data["days"])
        final_salary = add_bonus(base_salary)
        print(f"{name}: {final_salary:.2f} грн")

    print("\n Список співробітників:")
    print_employees_recursive(list(employees.keys()))


if __name__ == "__main__":
    main()
