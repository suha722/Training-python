'''Task 1 - Gradebook
In this task, we'll create a program that allows a teacher to keep track of the grades for their students.
The program will store and manipulate the data. Here are the features we'll include:

Add a new student to the gradebook.
Add a new assignment to the gradebook for all students.
Add a grade for a student for a specific assignment.
Calculate the average grade for a student.
Calculate the average grade for all students.
Print a report for a specific student showing all of their grades.
Print a report for all students showing their grades for all assignments.'''
Grade_book = {}


def add_student(name):
    Grade_book[name] = {'assignment': {}}


def add_assigment(homework):
    for studentname in Grade_book:
        Grade_book[studentname]['assignment'][homework] = []


def add_gradeforassigment(name, assigmentname, grade):
    Grade_book[name]['assignment'][assigmentname].append(grade)


def averge1student(name):
    avarage = 0
    totalgrade = 0
    assnum = 0
    for item in Grade_book[name]['assignment']:
        asstotal = Grade_book[name]['assignment'][item]
        totalgrade += sum(asstotal)
        assnum += len(asstotal)
        avarage = totalgrade / assnum
    return avarage


def avergeallstudent(func=averge1student):
    totalavarage = 0
    stdnum = 0
    for std in Grade_book.keys():
        totalavarage += func(std)
        stdnum += 1
    return totalavarage / stdnum


def report1student(name):
    print(f'{name} grades : ')
    for ass in Grade_book[name]['assignment']:
        print(f'{ass} : {Grade_book[name]["assignment"][ass]}')
    print(f'Average Grade: {averge1student(name)}')


def reportallstudent(func=report1student):
    for std in Grade_book.keys():
        func(std)


add_student("suha")
add_student("Ibrahim")
print(Grade_book)
add_assigment('homwork1')
add_assigment('homwork2')
add_gradeforassigment('suha', 'homwork1', 10)
add_gradeforassigment('suha', 'homwork1', 7)
add_gradeforassigment('suha', 'homwork2', 10)
add_gradeforassigment('Ibrahim', 'homwork1', 9)
add_gradeforassigment('Ibrahim', 'homwork1', 6)
print(Grade_book)
print(averge1student('suha'))
print(averge1student('Ibrahim'))
print(avergeallstudent())
report1student('suha')
reportallstudent()
