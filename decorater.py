#decorators class
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log
def greet(name):
    print(f"Hello, {name}!")

greet("John")
#Mixen class

class ToDictMixin:
    def to_dict(self):
        return vars(self)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person, ToDictMixin):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

employee = Employee("John", 30, 50000)
print(employee.to_dict())
