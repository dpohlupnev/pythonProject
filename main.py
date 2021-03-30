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

# метод выставления оценки лектору за лекции, добавляется в класс Lecturer, переменную student_grade (работает)
    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in lecturer.courses_attached:
            if course in lecturer.student_grade:
                lecturer.student_grade[course] += [grade]
            else:
                lecturer.student_grade[course] = [grade]
        else:
            return 'Ошибка'

# метод подсчета средней оценки студента за дз, поставленной проверящим, считается в этом же классе (не работает)
    def grade_student(self):
        sum_grade = []
        for grade in self.hw_grade.items():
            sum_grade.extend(grade[1])
        self.average_rating_stud = str(round(sum(sum_grade) / len(sum_grade), 1))
        return self.average_rating_stud

# перезагрузка магического метода lt (less than) для сравнения двух студентов (не работает, т.к. не дописан, непонятно как сразу вывести на экран результат сравнения)
    def __lt__(self, other_stud):
        if isinstance(other_stud, Student):
            if other_stud.average_rating_stud < self.average_rating_stud:
                print(f'Лучший студент! {self.name}')
                print(f'Худший студент {other_stud.name}')
        else:
            return f"{other_stud.name} Не является студентом!"

# перезагрузка магического метода str (работает)
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

# метод подсчета средней оценки лектора за лекции, поставленной студентом, считается в этом же классе (не работает)
    def grade_lec(self):
        sum_grade = []
        for grade in self.student_grade.items():
            sum_grade.extend(grade[1])
        self.average_rating_lec = str(round(sum(sum_grade) / len(sum_grade), 1))

        return self.average_rating_lec

# перезагрузка магического метода lt (less than) для сравнения двух лекторов (не работает, т.к. не дописан, непонятно как сразу вывести на экран результат сравнения)
    def __lt__(self, other_lec):
        if not isinstance(other_lec, Lecturer):
            print('Не является лектором!')
            if other_lec.average_rating_lec < self.average_rating_lec:
                self.name = 'Лучший лектор!'
        else:
            return f"{other_lec.name} Не является лектором!"

# перезагрузка магического метода str для лектора (работает)
    def __str__(self):
        return f"Лектор\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating_lec}\n"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

# метод выставления оценки студенту за дз, добавляется в класс Student, переменную hw_grade
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.hw_grade.keys():
                student.hw_grade[course] += [grade]
            else:
                student.hw_grade[course] = [grade]
        else:
            return 'Ошибка'

    # def grade_reviewer(self):
    #     sum_grade = []
    #     for grade in self.grades.items():
    #         sum_grade += grade[1]
    #     self.average_rating_stud = str(round(sum(sum_grade) / len(sum_grade)))
    #
    #     return self.average_rating_stud

# перезагрузка магического метода str для проверяющего (работает)
    def __str__(self):
        return f"Проверяющий\nИмя: {self.name}\nФамилия: {self.surname}\n"


one_student = Student('Ruoy', 'Eman', 'man')
one_student.courses_in_progress += ['Python', 'Git', 'Java', 'JavaScript']
one_student.finished_courses += ['Python', 'Git', 'Java', 'JavaScript']

two_student = Student('Mary', 'Kuri', 'women')
two_student.courses_in_progress += ['Python', 'Git', 'Java', 'JavaScript']
two_student.finished_courses += ['Python', 'Git', 'Java', 'JavaScript']

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
one_reviewer.rate_hw(one_student, 'Python', 8)
one_reviewer.rate_hw(two_student, 'Git', 4)

two_reviewer = Reviewer('Katy', 'Perry')
two_reviewer.courses_attached.append('Python')
two_reviewer.rate_hw(one_student, 'Python', 1)
two_reviewer.rate_hw(two_student, 'Git', 8)

one_student.grade_student()
one_student.average_rating_stud

# two_student.grade_student()
# two_student.average_rating_stud

print(one_student)
print(two_student)
print(one_lecturer)
print(two_lecturer)
print(one_reviewer)
print(two_reviewer)

# one_student < two_student

# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)