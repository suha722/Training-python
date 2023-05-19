# set &tuple
"""
Write a function that takes two sets as input and returns a new set containing only the
 elements that are in both sets.
"""
from numpy import sort

#
# def intersection(set1, set2):
#     return set1.intersection(set2)
#
#
# set1 = {1, 2, 3, 4, 5}
# set2 = {1, 5, 6, 8}
# print(intersection(set1, set2))

"""
Write a function that takes a tuple and an element as input and returns True if the
element is in the tuple, and False otherwise.
"""
#
#
# def search_in_tuple(tuple_data, element):
#     return element in tuple_data
#
#
# data = (1, 2, 3, 4, 5)
# element = 5
# print(search_in_tuple(data, element))

"""
Write a function that takes a list as input and returns a new list with all the duplicate elements 
removed, using sets.
"""

#
# def removed_duplicate(list_data):
#     return set(list_data)
#
#
# data = [1, 2, 3, 4, 4, 4, 5, 5, 6, 7, 8, 8, 9, 9, 9, 5, 4]
# print(removed_duplicate(data))


"""
Write a function that takes a list of tuples and an integer as input, and returns a new list of tuples sorted by 
the element at the specified index.
"""

#
# def sort_list_of_tuple(data, index):
#     data.sort(key=lambda a: a[index])
#     return data
#
#
# data = [(1, 6), (3, 4), (6, 1)]
# index = 1
# print(sort_list_of_tuple(data, index))


"""
Write a function that takes two sets as input and removes all the elements from the first set
that are not in the second set.
"""

# def remove_set(set1,set2):
#     diffrence=set1-set2
#     for num in diffrence:
#         set1.remove(num)
#     return set1
#
# set1= {1, 2, 3}
# set2= {1, 4, 5}
# print(remove_set(set1,set2))

"""
Write a function that takes a list of tuples as input and returns a new list of tuples, where each tuple is sorted 
in ascending order by the second element.
"""


# def sorted_ascending_list_of_tuple(data):
#     new_list = sorted(data, key=lambda a: a[1])
#     return new_list
#
#
# data = [(1, 16), (3, 8), (6, 24)]
# print(sorted_ascending_list_of_tuple(data))
