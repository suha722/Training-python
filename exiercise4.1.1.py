"""
Simple Bank Account: Create a BankAccount class that has two attributes: balance and owner.
The class should have two methods: deposit(amount) and withdraw(amount), which modify the balance accordingly.
Implement encapsulation by making the balance attribute private.
"""
from _distutils_hack import override

'''class Bank_Account:
    def __init__(self, balance, owner):
        self.__balance = balance
        self.owner = owner

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print(f"you don't have this amount of many your monay is only : {self.__balance}")
        else:
            self.__balance -= amount
    def get_balance(self):
        return self.__balance
firstaccount=Bank_Account(1000,'Zeyad')
print(firstaccount.get_balance())
# firstaccount.deposit(99)
# firstaccount.withdraw(100)
# print(firstaccount.get_balance())'''

"""
Person: Create a Person class with attributes name and age. Add a method birthday() that increments the person's 
age by one. Then create a Student class that inherits from Person and adds an attribute student_id and a method 
enroll(course) that prints the message "Enrolling {course} for {name} (ID: {student_id})".

"""

'''class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def brthday(self,age):
        self.age+=1
class Student(Person):
    def __init__(self,name,age,student_id):
        self.student_id=student_id
        super().__init__(name,age)
    def enroll(self,course):
        print(f"Enrolling {course} for {self.name} (ID: {self.student_id}).")

# p=Person("Suha",20)
s=Student("suha",20,132)
s.enroll("java")'''

"""
Shapes: Create a Shape class with a method area() that returns the area of the shape.
Then create two subclasses Rectangle and Circle that override the area() method to return the area of the 
corresponding shape. Create a function get_shape_area(shape) that takes a shape object as input and returns
its area.

"""

'''class Shap:


    def __init__(self):
        pass

    def area(self):
        return 0

    def get_shape_area(self, shap):
        return shap.area()


class Circular(Shap):
    def __init__(self, radius):  # 2pi *r
        self.radius = radius
        super().__init__()

    def area(self):
        return self.radius ** 2 * 3.14
        self.radius


class Rectangle(Shap):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        super().__init__()

    def area(self):
        return self.width * self.length


s = Shap()
r = Rectangle(10, 10)
c = Circular(2)

print("The area of circular is :", s.get_shape_area(c), "\n The area of rectangle is : ", s.get_shape_area(r))
'''

"""
Person with Encapsulation Create a Person class with attributes name and age. Implement encapsulation by 
making the age attribute private.Add a method birthday() that increments the person's age by one.

"""

'''
class Person:
    def __init__(self, name, age):
        self.name = name
        
        self.__age = age

    def birthday(self):
        self.__age += 1
    def get_age(self):
        return self.__age
p=Person("Hamed",20)
p.birthday()
print(p.get_age())
'''

"""
Vehicle: Create a Vehicle class with attributes make, model, and year. Add a method get_info() that 
returns a string with the vehicle's make, model, and year. Then create a Car class that inherits from Vehicle
 and adds a method accelerate(speed) that prints the message "The car is accelerating to {speed} mph

"""
class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def get_info(self):
        return f"vehicle's {self.make} ,model {self.model} ,year {self.year}"
class Car(Vehicle):
    def __init__(self,make,model,year,speed):
        super().__init__(make,model,year)
        self.speed=speed
    def accelerate(self):
        return f"The car is accelerating to {self.speed} mph"

c=Car("ford",2001,200,100)
print(c.get_info())
print(c.accelerate())