"""
Exercise 1: Handle division by zero exception Write a Python program that takes two numbers as input from the user
 and performs division. Handle the ZeroDivisionError exception in case the second input_number is zero.

 Ask the user to input two numbers and store them in variables num1 and num2.
Use a try-except block to handle the ZeroDivisionError.
In the try block, divide num1 by num2 and store the result in a variable result.
In the except block, print an error message indicating that division by zero is not allowed.
Finally, print the result of the division.
"""
import math

'''class Calculate:
    """
    this class have two function first for rnter the input_number the second to divion the two input_number
    """
    def input_number(self):
        """
        this function allow the user to input the input_number you want to division
        :return: tuple of the input_number entered
        """
        num1=0
        num2=0
        try:
            num1=int(input("Enter the first input_number: "))
            num2=int(input("Enter the second input_number: "))
        except ValueError:
            print("Please enter input_number only!")
        return num1,num2
    def division(self):
        """
        this function call function entered input_number and use this input_number to division if can and print the result        :return:  of division
        """
        result=0
        num1,num2=self.input_number()
        try:
            result=num1/num2
            print(f"{num1} / {num2} = ",result)
        except ZeroDivisionError :
            print("You can't division by zero! ")


cal=Calculate()
cal.division()
'''
""""
Exercise 2: Handle invalid input exception Write a Python program that prompts the user to enter a input_number
 between 1 and 10. If the user enters an invalid input, such as a string or a input_number 
 outside the range, handle the ValueError exception.
"""
'''def input_user():
    """
    this function check the input user where the boundaries are entered the integer between 1-10 only 
    :return: print the input_number if it is integer and in range 10 
    """
    while True:
        try:
            input_number=int(input("Enter the input_number:"))
            if input_number not in range(11):
                print("Enter the input_number between 1 to 10 only")
            else:
                print("The input_number is valid :",input_number)
                break

        except ValueError:
            print("Enter input_number only")

input_user()
'''
"""
Exercise 3: Handle file not found exception Write a Python program that prompts the user for a filename and 
reads the contents of the file. If the file does not exist, 
handle the FileNotFoundError exception.
Prompt the user for a filename and store it in a variable filename.
Use a try-except block to handle the FileNotFoundError.
In the try block, open the file and read its contents.
In the except block, print an error message indicating that the file was not found.
Finally, close the file and print its contents.

"""

'''def read_file():
    """
    this function read the file if found it
    :return: print the contains of the file
    """
    input_file=input("Enter the file name:")
    try:
        with open(input_file,"r")as file:
            for line in file:
                print(line)
    except FileNotFoundError as e:
        print("Sorry the file not found!")
read_file()'''

"""
Exercise 4: Custom exception handling Define a custom exception class NegativeNumberError that is raised if
 a negative number is passed to a function that is supposed to calculate the square root of the number. 
 Write a Python program that uses this custom exception to handle negative inputs.

"""
import math


class NegativeNumberError(ValueError):
    def square_root(self, number):
        if number < 0:
            raise NegativeNumberError("The input number is negative!")

        return math.sqrt(number)

    def input_number(self):
        try:
            enter_number = int(input("Enter the input_number to find the squre root for it "))
            # return enter_number
            print(NegativeNumberError.square_root(self,enter_number))
        except ValueError as e:
            print(e)
            return 0


findsqr = NegativeNumberError()
try:
    findsqr.input_number()
except NegativeNumberError as e:
    print(e)