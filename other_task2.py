"""
Task 2
Description
Your task is to write a Python program that reads log files from a given directory, filters out records that
contain the keywords "error" or "exception", and then calculates the frequency of occurrence of each remaining
keyword across all the log files.
The log files contain records in the format (timestamp, message), where timestamp is a string representing
the date and time of the log entry, and message is a string containing the log message. A record is considered
to contain an error if the message string contains the keyword "error" or "exception", regardless of case.
The program should output a list of keywords and their frequency of occurrence across all the log files.
 The list should be sorted alphabetically by keyword.
Requirements
To complete this task, you will need to use the following Python features:
Tuples
Sets
Lambda functions
Generators
System design
In particular, you will need to use generators to read the log files and filter out records that contain errors.
You will also need to use a set to keep track of the unique keywords, and a dictionary to keep track of the frequency
of occurrence of each keyword.
Your program should meet the following requirements:
It should take the path to the log directory as a command-line argument.
It should read all the log files in the directory and process them as described above.
It should output the list of keywords and their frequency of occurrence across all the log files, sorted
alphabetically by keyword.
It should handle any errors that may occur during the processing of the log files, such as file not found
errors or permission errors.
It should be well-documented and easy to understand.
Input Example
file1.log
2023-05-10 12:01:32 INFO: Starting server
2023-05-10 12:02:05 WARNING: Disk space low
2023-05-10 12:03:12 ERROR: Out of memory
file2.log
2023-05-10 12:05:01 INFO: User login successful
2023-05-10 12:05:15 WARNING: Invalid password attempt
2023-05-10 12:05:37 ERROR: Database connection failed
file3.log
2023-05-10 12:08:02 INFO: New request received
2023-05-10 12:08:27 WARNING: Request took too long
2023-05-10 12:09:12 ERROR: Internal server error
Example output
Starting 1
server 1
Disk 1
space 1
low 1
User 1
login 1
successful 1
Invalid 1
password 1
attempt 1
Database 1
connection 1
failed 1
New 1
request 1
received 1
took 1
too 1
long 1
Internal 1
server 1
"""
import fnmatch
import os
import re
import time
from time import sleep

import argparse

parser = argparse.ArgumentParser(description="A script that demonstrates argument groups")
input_group = parser.add_argument_group("Input Options", "Options related to input data")
input_group.add_argument("-i", "--input-file", type=str, help="Path to the input file")
args = parser.parse_args()
def log_reader(directory):
    filename = " "
    filepos = 0
    pattern = re.compile('[a-z?0-9]+\.log')
    for afile in os.listdir(directory):
        # print(afile)
        if pattern.match(afile):
            # print(afile)
            with open(afile,'r')as f:
                while True:
                    line = f.readline()
                    if not line:
                        # time.sleep(0.1)
                        continue


                    yield line

def punctuation_lower_filter(string):
    """
    this function take string filtered from punctuation and ignore the lower case
    :param string:
    :return:filtered string
    """
    # punctuation marks
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    # traverse the given string and if any punctuation
    # marks occur replace it with null
    for word in string.lower():
        if word in punctuations:
            string = string.replace(word, "")

    # return string without punctuation and ignoring case
    return string.lower()


def filtered_data(data):
    """
    this function call the data filter function and pass the string to filtered it
     and define set and dictionary to return a dictionary of
    word and count of each word and set of unique word only
    :param data:string
    :return: tuple of dictionary contains word as a key  and their count as a value and
    the second element in  the tuple is set of unique word
    """
    counts_word = dict()
    unique_word = set()
    data_filter = punctuation_lower_filter(data)
    words = data_filter.split()
    for word in words:
        if word in counts_word:
            counts_word[word] += 1
        else:
            counts_word[word] = 1
    for word in words:
        if counts_word[word] == 1:
            unique_word.add(word)
    return unique_word, counts_word
data=[]
dir = "C:/Users/ADMIN\PycharmProjects/pythonProject/Week6/"
obj=log_reader(directory=dir)

# print(next(obj).split(' :'))
for word in obj:
    if word.__contains__("ERROR") or word.__contains__("Exception"):
        print("cointaines error")
    else:

        line=word.split(': ')
        output_string,countword=filtered_data(line[1])
        # print(sorted(output_string))
        for word in countword:
            print(word,countword.__getitem__(word))
            data.append(word)
    sortedalphapet=sorted(data)
    print(sortedalphapet)
