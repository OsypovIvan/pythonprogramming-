from student import Student
from academic import Academic, DesiredAcademic


class StudentData:
    def __init__(self, student: Student, real_academic: Academic, desired_academic: DesiredAcademic):
        self.student = student
        self.real_academic = real_academic
        self.desired_academic = desired_academic

    def get_real_average(self):
        return self.real_academic.average_score()

    def get_desired_average(self):
        return self.desired_academic.average_score()

    def insert(self, db):
        db.insert_data(
            "students",
            ["full_name", "group_number", "birth_date", "address", "subjects", "scores", "desired_scores"],
            [
                self.student.get_full_name(),
                self.student.get_group_number(),
                self.student.get_birth_date(),
                self.student.get_address(),
                ",".join(self.real_academic.subjects),
                ",".join(map(str, self.real_academic.scores)),
                ",".join(map(str, self.desired_academic.scores))
            ]
        )

    def partial_update(self, db, table, updates: dict, student_id):
        set_clause = ", ".join([f"{key} = ?" for key in updates.keys()])
        sql = f"UPDATE {table} SET {set_clause} WHERE id = ?"
        params = list(updates.values()) + [student_id]

        cursor = db.cursor()
        cursor.execute(sql, params)
        db.commit()

    def delete_student(self, db, table, student_id):
        sql = f"DELETE FROM {table} WHERE id = ?"

        try:
            cursor = db.cursor()
            cursor.execute(sql, (student_id,))
            db.commit()
            print(f"Студент з ID {student_id} успішно видалений.")
        except Exception as e:
            print(f"Помилка при видаленні студента: {e}")