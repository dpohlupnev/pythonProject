class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in lecturer.courses_attached:
            if course in lecturer.student_grade:
                lecturer.student_grade[course] += [grade]
            else:
                lecturer.student_grade[course] = [grade]
        else:
            return 'Ошибка'

    def grade_student(self):
        sum_grade = []
        for grade in self.grades:
            

    def __str__(self):
        return f"Студент\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: \nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}\n"

    def __lt__(self, other):
        if self.grades < other.grades:
            return 'worst_student'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.student_grade = {}
        super().__init__(name, surname)

    def __str__(self):
        return f"Лектор\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: \n"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Проверяющий\nИмя: {self.name}\nФамилия: {self.surname}\n"


one_student = Student('Ruoy', 'Eman', 'man')
one_student.courses_in_progress += ['Python', 'Git']
one_student.finished_courses += ['Java', 'JavaScript']

two_student = Student('Mary', 'Kuri', 'women')
two_student.courses_in_progress += ['Java', 'JavaScript']
two_student.finished_courses += ['Python', 'Git']

one_lecturer = Lecturer('Some', 'Buddy')
one_lecturer.courses_attached += ['Python', 'Git', 'Java', 'JavaScript']

two_lecturer = Lecturer('Piter', 'Jackson')
two_lecturer.courses_attached += ['Python', 'Git', 'Java', 'JavaScript']

one_student.rate_lec(one_lecturer, 'Java', 8)
one_student.rate_lec(one_lecturer, 'JavaScript', 4)

two_student.rate_lec(two_lecturer, 'Python', 10)
two_student.rate_lec(two_lecturer, 'Git', 7)

one_reviewer = Reviewer('Jay', 'Simpson')

two_reviewer = Reviewer('Katy', 'Perry')

print(one_student)
print(two_student)
print(one_lecturer)
print(two_lecturer)
print(one_reviewer)
print(two_reviewer)

# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)