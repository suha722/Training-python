# Write a Python function that takes two lists of integers and returns a new list that contains
# only the elements that are common between the two lists.
def common_elements_in_lists(list1, list2):
    """
    this function found the common items in two list and appand the common in another list
    :param list1: list of integer
    :param list2: list of integer
    :return: list containes of common item from two list
    """
    commonlist=[]
    for item in list1:
        if item in list2:
            commonlist.append(item)
    return commonlist


list1=[1,-2,3,45,65]
list2=[-2,4,5,1,1,45]
print("The common element between the two list is: \n",common_elements_in_lists(list1,list2))



# Write a Python function that takes a string and returns a dictionary where the keys are the individual
# characters in the string and the values are the input_number of times each character appears in the string.
def dictionary_from_string(sentences):
    """
    this function receive   a string and return a dictionary of each character in the sentaece as key
    and value how many repeater
    :param sentences:
    :return: (dictionary)dictionary of char as key and these frequencies as a value
    """
    dictonary_of_string = {}
    for char in sentences:
        if char.isalpha():
            if char in dictonary_of_string:

                dictonary_of_string[char] += 1
            else:
                dictonary_of_string[char] = 1
    return dictonary_of_string


print("The new dictionary : \n ",dictionary_from_string("hello world"))


# Write a Python function that takes a list of dictionaries, where each dictionary represents a person
# with keys for "name", "age", and "occupation", and returns a new list of only the names of people
# who are over the age of 30 and have an occupation of "engineer"
# [{"name": "", "age": 0, "occupation": ''}, {}]
def person_details(list_dictionary):
    """
    this function read a list of dictionary that have a person details and return a list of name of pepole the age is large than 30 years
    and this occupation is engineered
    :param list_dictionary:
    :return: list of name of pepole
    """

    newlist = []
    for item in range(len(list_dictionary)):
        if list_dictionary[item]["age"] > 30:
            if list_dictionary[item]["occupation"] == 'engineer':
                newlist.append(list_dictionary[item]["name"])
            # print(newlist)
    return newlist


list_dictionary_detils = [{"name": "Suha ", "age": 31, "occupation": 'engineer'},
                          {"name": "Ibrahim ", "age": 33, "occupation": 'engineer'},
                          {"name": "khailed ", "age": 28, "occupation": 'engineer'},
                          {"name": "Ahmad ", "age": 32, "occupation": 'accounting'}]
print("The person how age larger than 30 and occupation is engineer is :\n",person_details(list_dictionary_detils))


# Write a Python function that takes a list of tuples, where each tuple contains two strings, and returns
# a dictionary where the keys are the first string in each tuple and the values are lists of the second
# strings that appeared with that key.
# [("","")]
def list_of_tupel(list_tuple):
    """
    this function return dectionary from key the first string in tuple and the value is second of
    elements in tuple
    :param list_tuple: tuple in the list
    :return: (dictionary): from the elements of tuple
    """
    dictionary_form_tuple = {}
    for item in range(len(list_tuple)):
        dictionary_form_tuple[list_tuple[item][0]] = list(list_tuple[item][1])
    return dictionary_form_tuple


list_tuple = [("suha", "alardah"), ("Khaled", "Waleed"), ("Apple", "banana")]
print(list_of_tupel(list_tuple))


# Write a Python function that takes a list of integers and returns the second-largest input_number in the list.
def second_largest_in_list(list_of_integer):
    """
    this function return the second largest input_number in the list
    :param list_of_integer: list of integer
    :return: the second largest input_number from the list
    """

    list_of_integer.sort()
    second_largest=list_of_integer[-2]
    return second_largest
list=[-1,-2,0,9,9]
print("The second largest in the list :",second_largest_in_list(list))



# Write a Python function that takes a list of integers and returns a new list where each element is the
# sum of the original list up to that point.
# [1,2,3,4,5]->[1,3,6,10,15]
def sum_new_list(list):
    """
    this function receive list of integer and return a new list where each element is the
            sum of the original list up to that point.
    :param list: list of integer
    :return: return new list where each element is the
            sum of the original list up to that point.
    """
    new_list = []

    for item in range(len(list) + 1):
        total = 0
        for i in range(item):
            total += list[i]

        new_list.append(total)

    return new_list


list = [1, 2, 3, 4, 5]
print("The sum :",sum_new_list(list))
