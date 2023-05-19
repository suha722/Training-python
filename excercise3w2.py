"""the user must enter the list of input_number only to find the summation and standard deviation of
 the numbers
 1-first ask the user input_number of input_number you want to add_book in the list
 2-make for loop from range of input_number entred previous  and  enter all input_number and added
 it to the  list of input_number and use try and except to force the user enter the input_number
 3-we use built in function to find the summation of the list
 4-we use the stastics function which contines the mean and standerd_divation
 """
import random
import statistics
import string

'''#define the verible we want to uses
list_of_number = []
summation = 0
mean = 0
standerd_divation = 0
#ask the user how many input_number you want to add_book in the list
number_of_number=input("how many input_number you want to add_book")
try:
    #casting the enterd user to the input_number
    number_of_number = int(number_of_number)
    for num in range(number_of_number):
        input_number = input(" please enter the input_number : ")
        try:
            input_number = int(input_number)
            #add_book the input_number enter to the list
            list_of_number.append(input_number)
            #find the summation of the list using built in function
            summation = sum(list_of_number)
            #find the mean of the list using built in function
            mean = statistics.mean(list_of_number)
            #find the standerd_divation of the list using built in function
            standerd_divation = statistics.stdev(list_of_number)
        except ValueError:
            print("please enter input_number only")

except ValueError:
    print("please enter positive input_number")
#the result of summation the list and mean and standerd_divation
print(list_of_number, "the summation", summation, "the mean",mean,"standerd_divation",standerd_divation )
'''
# Write a program that generates a random password of a specified length.
"""
This program generate random password of a specified length it entered from the user and 
make validate enter input_number only use built in function to generate letter, hexidigits and spaical characters
 from string.generate the password and join it 
"""
'''password_length = input("enter the length of your password ")
password = ''
try:
    password_length = int(password_length)
    letter = string.ascii_letters
    number_and_spacial = string.hexdigits + string.punctuation
    password = ''.join(random.choice(letter and number_and_spacial) for num_letters in range(password_length))
    print("The password of length is", password_length, " is generated : ", password)
except ValueError:
    print("enter input_number only")
    

'''

# Write a program that reads a text and calculates the frequency of each word in the file.
# Use texts of your own
'''def find_frequency_sentence(sentence):
    """
    returns:
        the frequency of each word

    Args:
        sentence(string):a sentence contain many word
    return(dictionary):
        the word and his frequency in the sentances
    """
    dictionary_word={}
    for word in sentence.split():
        if word in dictionary_word:
            dictionary_word[word] += 1
        else:
            dictionary_word[word] = 1
    return dictionary_word
sentance="suha hi suha suha hi who are you iam 22 years old"
print(find_frequency_sentence(sentance))
'''


# Example 1: Improve Comments and Variable Names


# This program reads a list of integers and returns the sum
# Define the input list
# numbers = [1, 2, 3, 4, 5]
#
# # Calculate the sum of the numbers
# total = sum(numbers)
#
# # Print the sum
# print(f"The total is: {total}")
def sum_of_list(list_of_number: list) -> list:
    """
    returns:
        the sum of a list of numbers.
    param:
        list_of_number(list) : A list of numbers to be summed.
    return:
        (float):the sum of the input_number in the list
    """
    return sum(list_of_number)


# Example 2: Use List Comprehension to Simplify the following Code
# Given a list of strings, create a new list with the first letter of each string capitalized
# words = ['apple', 'banana', 'cherry']
#
# new_words = []
# for word in words:
#     new_word = word.capitalize()
#     new_words.append(new_word[0])
#
# print(new_words)
words = ['apple', 'banana', 'cherry']
newlist = [word.capitalize()[0] for word in words]
print(newlist)
