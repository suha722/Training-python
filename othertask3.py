# """
# Task 3
# Task Description
# Your task is to write a Python program that takes a list of strings as input and returns the two strings that
#  have the largest number of common letters.
# The program should use tuples to represent pairs of strings, sets to store the unique letters in each string,
#  a lambda function to compute the number of common letters between two strings, and generators to iterate over
#  the pairs of strings.
# Requirements
# To complete this task, you will need to use the following Python features:
# Tuples
# Sets
# Lambda functions
# Generators
# System design
# Your program should meet the following requirements:
# It should take a list of strings as input.
# It should compute the two strings that have the largest number of common letters.
# It should output the two strings and the number of common letters between them.
# It should handle any errors that may occur during the processing of the input, such as invalid input types
# or empty lists.
# It should be well-documented and easy to understand.
# Example Input
# ['hello', 'world', 'python', 'java', 'ruby']
# Example Output
# ('hello', 'world', 3)
#
# """
# from functools import reduce
#
#
# def largest_common(strings):
#     for i  in range(len(strings)):
#         for word in strings:
#             # newlist=reduce(largest_common,word)
#             # print(newlist)
#             string1 = strings[i]
#             string2 = strings[i+1]
#             s1 = set(string1)
#             s2 = set(string2)
#             common_char = s1 & s2  # Letters in both s1 and s2
#             print(common_char)
#     # for word in list_string:
#     #     print(word.split(' '))
#     #     print()
#     #     # if word.split() in word[1].split():
#     #     #     print(word.split(''))
#     # counts_word = dict()
#     # unique_word = set()
#     # for word in list_string:
#     #     if word in counts_word:
#     #         counts_word[word] += 1
#     #     else:
#     #         counts_word[word] = 1
#     # for word in list_string:
#     #     if counts_word[word] == 1:
#     #         unique_word.add(word)
#     # print(counts_word)
#     # print(unique_word)
# input= ["apple", "app", "ape",'banana']
# obj=map(largest_common,input)
# for value in obj:
#     print(value)
#
# print({c for c in input[0] if all(c in s for s in input[1:])})
# obj=map(lambda x:)
x = 'stringx'
y = 'stringy'
def inters(str1,str2):
    common = list(set([c for c in x if c in y]))
    print(common)
