# class Library_Management:
#     def __init__(self,name,author,year):
#         self.name=name
#         self.author=author
#         self.year=year
#         # self.pathfile="book.json"
#
#     def add_book(self):
#
#         # with open(self.pathfile, "r") as file:
#         #     data=file.read()
#         #     for line in data:
#         #         for length in range(len(line)):
#         #             data[length]["name"] = self.name
#         #             data[length]["author"] = self.author
#         #             data[length]["year"] = self.year
#             # data={"name":self.name,"author":self.author,"year":self.year}
#             #
#             # file.write(data)
#         # with open(self.pathfile, "r") as file1:
#         #     for l in file1:
#         #         print(l)
#
#     def remove(self,name):
#         with open(self.pathfile, "w") as file:
#             for line in file:
#                 for length in range(len(line)):
#                     if line[length]["name"]==name:
#                         del line[length]
#                         file.write(line)
#     # def barrowing_book(self):
# lm=Library_Management("ahed","khaled",1990)
# lm.add_book()
# # lm.remove("ahed")
#
#
"""class Book:
    def __init__(self, b_name, author):
        self.name = b_name
        self.author = author
        self.list_book = []


class LibraryManagement(Book):

    def add_book(self, book, user):
        if user.authorized():
            # tu=(book,user)
            # self.list_book.append(tu)
            user.access_data()
            print(f"Added {book} to {user.name}.")
        else:
            print(f"Error: Only administrators can add books.")

    def removed_book(self, book, user, num):
        if user.authorized():
            # for l in self.list_book:
            #     del self.list_book[num]
            print(f"Removed The {book} by {user.name}.")
        else:
            print(f"Error: User {user.name}is not authorized to removed books.")

    def barrowing_book(self, book, user):
        if user.authorized():
            print(f"Borrowed {book} by {user.name}")
        else:
            print(f" Error: User {user.name} is not authorized to return books.")

    def returining_book(self, book, user):
        print(f" Returned {book} by {user.name}")


class User:
    def __init__(self, name):
        self.name = name

    def access_data(self):
        if self.authorized():
            print("We access to data of the book successfully! \n"
                  "____________________________________________")

    def authorized(self):
        if self.name == "AHMAD":
            return True
        else:
            return False


class Facade:
    def __init__(self):
        self.user = User("Khalel")
        self.user1 = User("AHMAD")
        self.book = LibraryManagement("Nabd", "Adham Sharqawe")

    def start_project(self):

        self.book.add_book("book1", self.user1)
        self.book.barrowing_book("book2", self.user)
        self.book.removed_book("book2", self.user1, 0)
        self.book.returining_book("book3", self.user1)


facade = Facade()
facade.start_project()

"""

from abc import ABC
class SortStrategy(ABC):
    def sort(self, data):
        pass
        
class BubbleSort(SortStrategy):
    def sort(self, data):
        print("Sorting using bubble sort")
        return sorted(data)
        
class QuickSort(SortStrategy):
    def sort(self, data):
        print("Sorting using quick sort")
        return sorted(data, key=lambda x: x)
        
class MergeSort(SortStrategy):
    def sort(self, data):
        print("Sorting using Merge sort")
        return sorted(data, key=lambda x: x)

class SortingContext:
    def __init__(self, setStrategy):
        self.strategy = setStrategy
        
    def sort(self, data):
        return self.strategy.sort(data)
    def setStrategy(self,strategy):
        self.strategy=strategy
        

data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

context = SortingContext(BubbleSort())
context.sort(data)
print(data)

context.setStrategy(MergeSort())
context.sort(data)
print(data)

context.setStrategy(QuickSort())
sorted_data = context.sort(data)
print(sorted_data)



