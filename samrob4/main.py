from db_manager import DBManager
from student import Student
from academic import Academic, DesiredAcademic
from student_data import StudentData

# Підключення до БД
db = DBManager("students.db")

# Створення таблиці
create_table_sql = """
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT,
    group_number TEXT,
    birth_date TEXT,
    address TEXT,
    subjects TEXT,
    scores TEXT,
    desired_scores TEXT
)
"""
db.create_table(create_table_sql)

while True:
    print("\nВиберіть операцію:")
    print("1 — Додати студента")
    print("2 — Редагувати студента")
    print("3 — Видалити студента")
    print("4 — Показати всіх студентів")
    print("0 — Вихід")

    choice = input("Ваш вибір: ").strip()

    if choice == "1":
        # Додавання
        full_name = input("Введіть ПІБ студента: ")
        group_number = input("Введіть номер групи: ")
        birth_date = input("Введіть дату народження (YYYY-MM-DD): ")
        address = input("Введіть адресу: ")

        subjects = []
        scores = []
        num_subjects = int(input("Скільки предметів у студента? "))
        for i in range(num_subjects):
            subject = input(f"Назва предмета #{i+1}: ")
            score = int(input(f"Оцінка за {subject}: "))
            subjects.append(subject)
            scores.append(score)

        desired_scores = []
        print("\nБажані оцінки:")
        for subject in subjects:
            desired = int(input(f"Бажана оцінка за {subject}: "))
            desired_scores.append(desired)

        student = Student(full_name, group_number, birth_date, address)
        real_academic = DesiredAcademic(subjects, scores)
        desired_academic = DesiredAcademic(subjects, desired_scores)
        student_data = StudentData(student, real_academic, desired_academic)
        student_data.insert(db)
        print("Студента додано.")

    elif choice == "2":
        # Редагування
        student_id = int(input("Введіть ID студента, якого хочете оновити: "))
        updates = {}
        print("\nВведіть нові значення (або залиште порожнім, щоб не змінювати):")

        full_name = input("Нове ПІБ: ")
        if full_name:
            updates["full_name"] = full_name

        group_number = input("Новий номер групи: ")
        if group_number:
            updates["group_number"] = group_number

        birth_date = input("Нова дата народження (YYYY-MM-DD): ")
        if birth_date:
            updates["birth_date"] = birth_date

        address = input("Нова адреса: ")
        if address:
            updates["address"] = address

        change_subjects = input("Хочете змінити предмети та оцінки? (так/ні): ").strip().lower()
        if change_subjects == "так":
            subjects = []
            scores = []
            num_subjects = int(input("Скільки предметів? "))
            for i in range(num_subjects):
                subject = input(f"Предмет #{i+1}: ")
                score = int(input(f"Оцінка за {subject}: "))
                subjects.append(subject)
                scores.append(score)
            updates["subjects"] = ",".join(subjects)
            updates["scores"] = ",".join(map(str, scores))

            desired_scores = []
            print("\nБажані оцінки:")
            for subject in subjects:
                desired = int(input(f"Бажана оцінка за {subject}: "))
                desired_scores.append(desired)
            updates["desired_scores"] = ",".join(map(str, desired_scores))

        student_data = StudentData(None, None, None)  # Пустий об'єкт для доступу до методу
        student_data.partial_update(db.conn, "students", updates, student_id)
        print("Дані студента оновлено.")

    elif choice == "3":
        # Видалення
        student_id = int(input("Введіть ID студента для видалення: "))
        confirm = input(f"Ви впевнені, що хочете видалити студента з ID {student_id}? (так/ні): ").strip().lower()
        if confirm == "так":
            student_data = StudentData(None, None, None)
            student_data.delete_student(db.conn, "students", student_id)
        else:
            print("Видалення скасовано.")

    elif choice == "4":
        # Вивід
        print("\nСписок студентів:")
        for row in db.fetch_all("students"):
            print(row)

    elif choice == "0":
        print("До побачення!")
        break

    else:
        print("Невірний вибір. Спробуйте ще раз.")

db.close()