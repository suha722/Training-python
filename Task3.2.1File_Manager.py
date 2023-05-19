"""
Task - File Manager
The "File Manager" project is a Python program that allows a user to manage files in a directory.
The program provides a menu-based interface that allows the user to perform various operations on the files,
such as creating a new file, renaming an existing file, deleting a file, listing all files,and searching
for a file by name.
"""
import os.path


def list_all_file(path):
    """
    this function print the all files in the path entered from the user
    :param path: the path of diroctory
    :return: print list of file in the specific path
    """
    print("The all file is :")
    num = 1
    list_of_file=os.listdir(path)
    for list in list_of_file:
        print(num, "_", list)
        num += 1


def create_new_file(filename):
    """
    this function create new file
    :param filename:
    :return: check if the file is not exist the file created if exist print this file actually exists
    """

    if os.path.exists(filename):
        print("this file is exist!")
    else:
        f = open(filename, "x")
        print("success to creating file!")


def rename_the_file(pastname, newname):
    """
    this function rename the file to new name
    :param pastname: past name of file
    :param newname: the new name you want to rename it
    :return: rename the file to new name
    """
    os.rename(pastname, newname)


def delete_file(namefile):
    """
    this function give the name of file you want to delete it
    :param namefile: (name file)
    :return: remove the file and print if success delete or not
    """
    if os.path.exists(namefile):
        os.remove(namefile)
        print("success to delete this file")
    # else:
    #     print("")


def serach_file(path, name):
    """
    this function search for the file you want
    :param path: the path of dirctory
    :param name: name of file you search it
    :return:  print a list the file if there are exists print no file if not exists
    """
    listfile = []
    for filename in os.listdir(path):
        if name in filename:
            listfile.append(filename)
    if len(listfile) == 0:
        print("Sorry we don't found the file !")

    else:
        print("the results of search it  :")
        for filefound in listfile:
            print(filefound)


def welcome_page():
    print("Welcome to File Manger program:")
    print(os.getcwd())
    path = input("Enter the path of the directory: ")
    choice = 0
    if os.path.exists(path):
        print("Menu: \n"
              "1. List all files \n"
              "2. Create a new file \n"
              "3. Rename a file \n"
              "4. Delete a file \n"
              "5. Search for a file \n"
              "6. Exit")
        while True:

            choice = input("Enter your chice")

            try:
                choice = int(choice)
                if choice == 1:
                    list_all_file(path)
                if choice == 2:
                    filename = input("Enter the file name :")
                    create_new_file(filename)
                if choice == 3:
                    pastname = input("Enter the name file you want to rename")
                    newname = input("Enter the new name ")
                    lists=os.listdir(path)
                    if newname in lists:
                        print("the file is already exists!")
                    else:
                        rename_the_file(pastname, newname)
                        print("success to rename the file!")
                if choice == 4:
                    name = input("Enter the name of file you want to delete: ")
                    delete_file(name)
                if choice == 5:
                    name_file = input("Enter the name of file you want to find : ")
                    serach_file(path, name_file)
                if choice == 6:
                    print("Good bye!")
                    break

            except ValueError:
                print("enter vailed choice please!")
    else:
        print("Sorry the path not found!")
welcome_page()