"""
Map Function

Description: Write a Python program to create a list of squares of all numbers in a
given list using the map function.
"""
from functools import reduce

numbers=[1,2,3,4,5,6,7,8,9]
square=map(lambda number:number**2,numbers)
list_square=list(square)
print(f"squares of all numbers of {numbers} is : ",list_square)
"""
Reduce Function

Description: Write a Python program to compute the product of all numbers in a given list using the 
reduce function.
"""

result=reduce(lambda num1,num2:num1*num2,numbers)
print(f"The result of product is the list using reduce {numbers} is :",result)
"""
List Comprehensions

Description: Write a Python program to create a list of squares of all even numbers in a given list
 using list comprehensions
"""
#
evennumber=[num**2 for num in numbers if num%2==0]
print(f"The squares of all even numbers of list {numbers} is :",evennumber)

"""
Recursion

Description: Write a Python program to calculate the factorial of a given number using recursion.
"""
def factorial(num):
    # check if the number is negative
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num==0 or num==1 :
        return num

    else:
        return num*factorial(num-1)
num=4
result=factorial(num)
print(f"The result of factorial {num} is :",result)

"""
Description: Write a Python function that takes a list of numbers and a function and applies the 
function to each number in the list.
"""
numbers=[1,2,3,4,5]
def sumlist(listnumber):
    for num in listnumber:
        print(num*2,end=' ')
def hof(listnumber,func):
    func(listnumber)
print("The result of higher order function is :")
hof(numbers,sumlist)

"""
Description: Write a Python function that takes a list of words and returns a list of their lengths that are greater 
than or equal to a given value."""
def filter_map(list_word,min_length):
    # for word in list_word:
    word_len=list(filter(lambda length:length>min_length,list(map(lambda word:len(word),list_word))))
    return word_len

my_words = ['alfred', 'tabitha', 'william', 'arla']
minlength=4
print(f"\n the length of the words in the list{my_words} and length <{minlength} :",filter_map(my_words,4))


"""
Description: Write a Python function that takes a number and generates the Fibonacci sequence up
 to that number using a generator.
"""


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

a=8
print(list(fib(a)))