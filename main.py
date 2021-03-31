class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.hw_grade = {}
        self.average_rating_stud = None

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

# метод выставления оценки лектору за лекции, добавляется в класс Lecturer, переменную student_grade
    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in lecturer.courses_attached:
            if course in lecturer.student_grade:
                lecturer.student_grade[course] += [grade]
            else:
                lecturer.student_grade[course] = [grade]
        else:
            return 'Ошибка'

# метод подсчета средней оценки студента за дз, поставленной проверящим, считается в этом же классе
    def grade_student(self):
        sum_grade = []
        for grade in self.hw_grade.items():
            sum_grade.extend(grade[1])
        self.average_rating_stud = str(round(sum(sum_grade) / len(sum_grade), 1))
        return self.average_rating_stud

# перезагрузка магического метода lt (less than) для сравнения двух студентов
    def __lt__(self, other_stud):
        if isinstance(other_stud, Student):
            return other_stud.average_rating_stud < self.average_rating_stud
        else:
            return f"{other_stud.name} Не является студентом!"

# перезагрузка магического метода str
    def __str__(self):
        return f"Студент\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_rating_stud}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}\n"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.student_grade = {}
        self.average_rating_lec = None
        super().__init__(name, surname)

# метод подсчета средней оценки лектора за лекции, поставленной студентом, считается в этом же классе
    def grade_lec(self):
        sum_grade = []
        for grade in self.student_grade.items():
            sum_grade.extend(grade[1])
        self.average_rating_lec = str(round(sum(sum_grade) / len(sum_grade), 1))

        return self.average_rating_lec

# перезагрузка магического метода lt (less than) для сравнения двух лекторов
    def __lt__(self, other_lec):
        if isinstance(other_lec, Lecturer):
            return other_lec.average_rating_lec < self.average_rating_lec
        else:
            return f"{other_lec.name} Не является лектором!"

# перезагрузка магического метода str для лектора
    def __str__(self):
        return f"Лектор\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating_lec}\n"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

# метод выставления оценки студенту за дз, добавляется в класс Student, переменную hw_grade
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.finished_courses:
            if course in student.hw_grade.keys():
                student.hw_grade[course] += [grade]
            else:
                student.hw_grade[course] = [grade]
        else:
            return 'Ошибка'

# перезагрузка магического метода str для проверяющего (работает)
    def __str__(self):
        return f"Проверяющий\nИмя: {self.name}\nФамилия: {self.surname}\n"


one_student = Student('Ruoy', 'Eman', 'man')
one_student.courses_in_progress += ['Java', 'JavaScript']
one_student.finished_courses += ['Python', 'Git']

two_student = Student('Mary', 'Kuri', 'women')
two_student.courses_in_progress += ['Python', 'Git']
two_student.finished_courses += ['Java', 'JavaScript']

one_lecturer = Lecturer('Some', 'Buddy')
one_lecturer.courses_attached += ['Python', 'Git', 'Java', 'JavaScript']

two_lecturer = Lecturer('Piter', 'Jackson')
two_lecturer.courses_attached += ['Python', 'Git', 'Java', 'JavaScript']

one_student.rate_lec(one_lecturer, 'Python', 5)
one_student.rate_lec(one_lecturer, 'Git', 8)
one_student.rate_lec(two_lecturer, 'Java', 3)
one_student.rate_lec(two_lecturer, 'JavaScript', 2)

two_student.rate_lec(one_lecturer, 'Python', 10)
two_student.rate_lec(one_lecturer, 'Git', 9)
two_student.rate_lec(two_lecturer, 'Java', 4)
two_student.rate_lec(two_lecturer, 'JavaScript', 5)

one_reviewer = Reviewer('Jay', 'Simpson')
one_reviewer.courses_attached.append('Python')
one_reviewer.courses_attached.append('Git')
one_reviewer.courses_attached.append('Java')
one_reviewer.courses_attached.append('JavaScript')
one_reviewer.rate_hw(one_student, 'Python', 8)
one_reviewer.rate_hw(one_student, 'Git', 2)
one_reviewer.rate_hw(two_student, 'Java', 7)
one_reviewer.rate_hw(two_student, 'JavaScript', 4)

two_reviewer = Reviewer('Katy', 'Perry')
two_reviewer.courses_attached.append('Python')
two_reviewer.courses_attached.append('Git')
two_reviewer.courses_attached.append('Java')
two_reviewer.courses_attached.append('JavaScript')
two_reviewer.rate_hw(one_student, 'Python', 1)
two_reviewer.rate_hw(one_student, 'Git', 3)
two_reviewer.rate_hw(two_student, 'Java', 8)
two_reviewer.rate_hw(two_student, 'JavaScript', 9)

one_student.grade_student()
two_student.grade_student()
one_lecturer.grade_lec()
two_lecturer.grade_lec()

print(one_student)
print(two_student)
print(one_lecturer)
print(two_lecturer)
print(one_reviewer)
print(two_reviewer)

print(one_student < two_student)
print(one_student > two_student)