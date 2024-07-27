class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        return f"Полная информация: {self.fullname}, Возраст: {self.age}, Семейное Положение: {'Есть' if self.is_married else 'Нет'}"


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def calculate_average(self):
        if not self.marks:
            return 0
        total_marks = sum(self.marks.values())
        number_of_subjects = len(self.marks)
        return total_marks / number_of_subjects


class Teacher(Person):
    base_salary = 50000

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        bonus = 0
        if self.experience > 3:
            bonus = (self.experience - 3) * (0.05 * Teacher.base_salary)
        return Teacher.base_salary + bonus



teacher = Teacher("Нурис Нурислам", 40, True, 10)

print(teacher.introduce_myself())
print(f"Опыт: {teacher.experience} лет")
print(f"Зарплата: ${teacher.calculate_salary():.2f}")


def create_students():
    student1 = Student("Джон Браун", 20, False, {"Math": 90, "English": 85, "Science": 88})
    student2 = Student("Адам Дуглас", 21, False, {"Math": 78, "English": 82, "History": 80})
    student3 = Student("Джон Смит", 22, False, {"Math": 92, "English": 89, "Geography": 94})

    return [student1, student2, student3]


students = create_students()
for student in students:
    print(student.introduce_myself())
    for subject, mark in student.marks.items():
        print(f"{subject}: {mark}")
    print(f"Average Mark: {student.calculate_average():.2f}")
