# Write a Python program to list all files in a directory.
# Write a Python program to find the largest file in a directory and its subdirectories.
# Write a Python program to calculate the total size of a directory and its subdirectories.

import os


def list_largest_total_size(path):
    """
    this function receive the path and find  list of file in this path and max size of file and total size
    :param path: path directory contains file and directory
    :return: print the list of file and max size and total size
    """

    os.chdir('/Users/ADMIN/PycharmProjects/pythonProject/Week3')
    list_dir = os.listdir()
    maxsize = os.stat('alphabetical_order_file.txt').st_size
    totalsize = 0
    print("The file in the path is : ")
    for size in list_dir:
        print(size)
        sizes = os.stat(size).st_size
        totalsize += sizes
        if sizes > maxsize:
            maxsize = sizes
    print("The max size file is :", maxsize, "\ntotal size : ", totalsize)


path = os.chdir('/Users/ADMIN/PycharmProjects/pythonProject/Week3')
list_largest_total_size(path)
