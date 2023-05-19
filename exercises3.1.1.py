# Write a Python program to read a list of strings from a text file, sort
# the strings in alphabetical order, and write the sorted list of strings to another text file.

def word_sorted_list():
    '''
    this functon read from file and convert the the line in file to list of string and find the sorted list in
    the list copy the result in another file
    :return:copy the sorted list in file name sorted_list_of_string.txt
    '''
    try:
        with open("alphabetical_order_file.txt", "r") as rf:
            with open("sorted_list_of _string.txt", "a") as wf:
                line = rf.readlines()
                # print(line)
                list_of_string_sorted = sorted(line)
                # print(list_of_string_sorted)
                for i in range(len(list_of_string_sorted)):
                    wf.write(list_of_string_sorted[i])

    except FileNotFoundError:
        print("Sorry the file not found!")
    except Exception as e:
        print("An error occurred:", e)


word_sorted_list()

# write_sorted_list_another_file()
# Write a Python program to count the input_number of words in a text file and display the count on the console.
'''def count_word_in_file(filename):
    """
    retuns:this read file and print the input_number of word in file
    :param:filename(file):the file we want to found input_number of word in it
    :return:print the input_number of words
    """
    count=0
    try:
        with open(filename, "r") as file:
            for content in file:
                line = file.read()
                words = [word.lower() for word in line.split()]
                for word in words:
                    count+=1
                print("The count of word in file is ",count)


    except FileNotFoundError:
        print("Sorry the file not found!")
    except Exception as e:
        print("An error occurred:", e)

# sort the list
count_word_in_file("alphabetical_order_file.txt")
'''
