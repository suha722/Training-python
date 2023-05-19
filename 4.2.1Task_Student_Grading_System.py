import random
from datetime import datetime


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Instructor(Person):
    def __init__(self, name, age, course_list):
        super().__init__(name, age)
        self.course_list = course_list

    def create_assessment(self):
        for course in self.course_list:
            course.students.append(course.assessments)


class Student(Person):
    def __init__(self, name, age, s_id, major, grade_level, enrolled_courses, enrolled_assessments):
        super().__init__(name, age)
        self.s_id = s_id
        self.major = major
        self.grade_level = grade_level
        self.enrolled_courses = enrolled_courses
        self.enrolled_assessments = enrolled_assessments

    def student_dict(self):
        student_dict = {"name": self.name, "age": self.age,
                        "student_id": self.s_id, "major": self.major, "grade": self.grade_level,
                        "enrolled_courses": self.enrolled_courses,
                        "enrolled_assessments": [self.enrolled_assessments[item].name() for item in
                                                 range(len(self.enrolled_assessments))]}
        return student_dict


class Courses:
    # ("Math",[h1,test],[s1,s2],[in1,n2])
    def __init__(self, name, assessments, students, instructors):
        self.name = name
        self.assessments = assessments
        self.students = students
        self.instructors = instructors

    def course_dict(self):
        course_dict = {"course_name": self.name,
                       "assessment": [self.assessments[item].name() for item in range(len(self.assessments))],
                       "student": [self.students[item].name for item in range(len(self.students))],
                       "instructor": [self.instructors[item].name for item in range(len(self.instructors))]}

        return course_dict


class Assessment:
    def __init__(self, questions, final_grade):
        self.questions = questions
        self.final_grade = final_grade


class Homework(Assessment):
    def __init__(self, questions, final_grade, due_date):
        super().__init__(questions, final_grade)
        self.due_date = due_date
    def generate_grade(self):
        self.final_grade=random.randint(0,10)
        return self.final_grade
    def name(self):
        return "Homework"
    # 20


class Exam(Assessment):
    def __init__(self, questions:list, final_grade:float, time:datetime):
        # quastion=[object MCQ,object TrueFalseQ]
        super().__init__(questions, final_grade)
        self.time = time
    def getgrade(self):
        for qus in self.questions:
            self.final_grade=qus.generate_grade()
        return self.final_grade

    def name(self):
        return "Exam"


class Test(Assessment):
    def __init__(self, questions, final_grade, time):
        super().__init__(questions, final_grade)
        self.time = time
    def getgrade(self):
        for qus in self.questions:
            self.final_grade=qus.generate_grade()
        return self.final_grade


    def name(self):
        return "Test"


class Question:
    def __init__(self, id, grade):
        self.id = id
        self.grade = grade


#
class MCQuestion(Question):
    def __init__(self, id, grade):
        self.id = id
        self.grade = grade

    def generate_grade(self):
        self.grade = random.randint(0, 20)
        return self.grade


class TFQuestion(Question):
    def __init__(self, id, grade):
        self.id = id
        self.grade = grade

    def generate_grade(self):
        self.grade = random.randint(0, 10)
        return self.grade


#
# def read_quastion(self,pathquestion,pathsoluation):
#         quastiondict={}
#         with open (pathquestion,"r")as file:
#             with open (pathsoluation,"r")as fileanswer:
#                 for line in file:
#                     if line.startswith("Q."):
#                         quastiondict[line]=fileanswer.readline().replace('\n','')
#         return quastiondict
#     def view_quastion(self,pathquestion,pathanswer):
#         grade=0
#
#         with open(pathquestion, "r") as file:
#             with open(pathanswer, "r") as fileanswer:
#                 for i in file:
#                     for length in range(5):
#                         ll= file.readline()
#                         print(ll)
#                     answer=input("Enter your answer")
#                     if answer==fileanswer.readline():
#                         grade+=1
#         print(grade)
#
#
# mq=MCQuestion()
#
# print(mq.read_quastion("MCQ.txt","answer.txt"))
# mq.view_quastion("MCQ.txt","answer.txt")
#

mq = MCQuestion(1, 0)
tf=TFQuestion(2,0)

# print(mq.generate_grade())
exam=Exam([mq],0,10)
test=Test([tf],0,20)
homework=Homework("[mq]",0,10)
print(exam.getgrade())
print(test.getgrade())
print(homework.generate_grade())


class Grader:
    def calculate_grade_for_student(self, stu1):  # 20,20,60 =100/100
        result = 0

        for grade in stu1.enrolled_assessments:
            result += grade.final_grade
        return result

    def calculate_assessment_final_grade(self, obj_course):
        # ("Math", [h1, test], [s1, s2], [in1, in2])
        result = 0
        for grade in obj_course.assessments:
            result += grade.final_grade
        return result


'''
g = Grader()
h1 = Homework("question", 20, 10)
test = Test("question", 19, 10)
stu1 = Student("suha", 22, 1, "Engineer", 4, ["Math", "C++"], [h1, test])
stu2 = Student("Ibrahim", 27, 1, "Engineer", 4, ["Math", "C++"], [h1, test])

course = Courses("Math", [h1, test], [stu1], ["in1", "n2"])
instructor = Instructor("Hossny", 43, [course])
print(g.calculate_grade_for_student(stu1))
cor = Courses("C++", [h1, test], [stu1, stu2], [instructor])
print(g.calculate_assessment_final_grade(cor))

print(instructor.course_list[0].students[0].enrolled_courses[1])
print(stu1.student_dict())
print(cor.course_dict())



Guide to creating UML Diagram from python code
there are many libraries to do that, I used the Pyreverse library(pyreverse analyzes your source code and generates package and class diagrams.), and here are a few steps to use library
1- install Giraphviz, you can download it from the official Graphviz website: https://graphviz.org/download/
2-Pyreverse is part of the pylint package, so you can install it using pip: pip install pylint
3- ensure that Graphviz is added to environment variables.
4 - Run pyreverse on your Python file(s) by typing pyreverse -o png .
The . specifies that pyreverse should generate a UML diagram for all python files in the current directory.
there is an extension on pycharm called PlantUML used for the same purpose
I hope that is useful

'''
