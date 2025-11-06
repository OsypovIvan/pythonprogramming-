def calculate_salary(salary, days):
    return (salary / 30) * days


def add_bonus(salary, bonus_percent=10):
    return salary + (salary * bonus_percent / 100)
