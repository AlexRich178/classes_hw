class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def _average_grade(self):
        grades_for_homeworks = self.grades.values()
        total_grade = 0
        grade_count = 0
        for i in grades_for_homeworks:
            total_grade += sum(i)
            grade_count += len(i)
        average_grade = round(total_grade / grade_count, 1)
        return average_grade

    def __str__(self):
        return f'Name: {self.name}' \
               f'\nSurname: {self.surname}' \
               f'\nAverage grade for homeworks: {self._average_grade()}' \
               f'\nCourses in progress: {", ".join(self.courses_in_progress)}' \
               f'\nCompleted courses: {", ".join(self.finished_courses)}\n '

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if grade in range(11):
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                print('Grade must be 0 - 10!')
        else:
            print(f"{self.name + ' ' + self.surname} is not allowed to rate {lecturer.name + ' ' + lecturer.surname}.")

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('You should compare student with other student!')
            return
        return self._average_grade() > other._average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_grade(self):
        grades_for_courses = self.grades.values()
        total_grade = 0
        grade_count = 0
        for i in grades_for_courses:
            total_grade += sum(i)
            grade_count += len(i)
        average_grade = round(total_grade / grade_count, 1)
        return average_grade

    def __str__(self):
        return f'Name: {self.name}' \
               f'\nSurname: {self.surname}' \
               f'\nAverage grade for lectures: {self._average_grade()}\n'

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('You should compare lecturer with other lecturer!')
            return
        return self._average_grade() > other._average_grade()


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
            print(f'{self.name + " " + self.surname} is not allowed to grade {student.name + " " + student.surname}.')

    def __str__(self):
        return f'Name: {self.name}\nSurname: {self.surname}\n'


# init Characters
alex_student = Student('Alex', 'Rich', 'male')
kate_student = Student('Kate', 'Sunny', 'female')

john_lecturer = Lecturer('John', 'Biggy')
anna_lecturer = Lecturer('Anna', 'Smith')

paul_reviewer = Reviewer('Paul', 'Saint')
emma_reviewer = Reviewer('Emma', 'Watson')

# init list of courses
john_lecturer.courses_attached += ['Python', 'Git', 'JavaScript', 'Frontend']
anna_lecturer.courses_attached += ['C++', 'C#', 'Backend', 'DataBase']

alex_student.courses_in_progress += ['Python', 'C#', 'Backend', 'JavaScript']
alex_student.finished_courses += ['Git', 'C++']

kate_student.courses_in_progress += ['C++', 'Git', 'Backend', 'JavaScript']
kate_student.finished_courses += ['Python']

paul_reviewer.courses_attached += ['Python', 'Git', 'Backend']
emma_reviewer.courses_attached += ['C++', 'C#', 'Fronted', 'JavaScript', 'DataBase', 'Backend']

# students grade the lecturers
alex_student.rate_lecturer(john_lecturer, 'Python', 9)
alex_student.rate_lecturer(john_lecturer, 'JavaScript', 7)
alex_student.rate_lecturer(anna_lecturer, 'C#', 10)
kate_student.rate_lecturer(john_lecturer, 'JavaScript', 8)
kate_student.rate_lecturer(john_lecturer, 'Git', 3)
kate_student.rate_lecturer(anna_lecturer, 'C++', 6)

# reviewers grade the students
paul_reviewer.rate_hw(alex_student, 'Python', 10)
paul_reviewer.rate_hw(alex_student, 'Backend', 2)
paul_reviewer.rate_hw(kate_student, 'Backend', 4)
paul_reviewer.rate_hw(kate_student, 'Git', 5)
emma_reviewer.rate_hw(kate_student, 'Backend', 6)
emma_reviewer.rate_hw(alex_student, 'C#', 8)
emma_reviewer.rate_hw(kate_student, 'C++', 7)

# info about Characters
print(john_lecturer)
print(anna_lecturer)
print(alex_student)
print(kate_student)
print(paul_reviewer)
print(emma_reviewer)

# compare Characters
print(john_lecturer < anna_lecturer)
print(f'{alex_student > kate_student}\n')


students = [alex_student, kate_student]
lecturers = [john_lecturer, anna_lecturer]


def average_grade_students_at_course(students, course):
    total_grade = 0
    grade_count = 0
    for student in students:
        if course in student.courses_in_progress:
            total_grade += sum(student.grades[course])
            grade_count += len(student.grades[course])
    try:
        average_grade = round(total_grade / grade_count, 1)
        print(f'Average grade by students at {course} is {average_grade}')
    except ZeroDivisionError:
        print(f'No {course} in progress or wrong course name.')


average_grade_students_at_course(students, 'Backend')


def average_grade_lecturer_at_course(lecturers, course):
    total_grade = 0
    grade_count = 0
    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            total_grade += sum(lecturer.grades[course])
            grade_count += len(lecturer.grades[course])
    try:
        average_grade = round(total_grade / grade_count, 1)
        print(f'Average grade by lecturers at {course} is {average_grade}')
    except ZeroDivisionError:
        print(f'No {course} in progress or wrong course name.')


average_grade_lecturer_at_course(lecturers, 'JavaScript')
