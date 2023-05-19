# Write a Python script that takes a single integer argument n and prints the first n Fibonacci
# numbers. Use argparse to handle the command-line argument.
'''
import argparse


parser=argparse.ArgumentParser(description="parsing argument to fibonacci")
parser.add_argument('term',help="The input_number in Fibonacci",type=int)
args=parser.parse_args()

def fibonacci(input_number):
        if input_number<=1:
            return input_number


        else:
            return fibonacci(input_number - 1)+fibonacci(input_number - 2)
            # num=n+n-1
            # print(num,end=" ")
input_number=args
for value in range(args.term):
    print(fibonacci(value),end=' ')
    '''

'''Write a Python script that takes two file paths as arguments, one for input and one for output, and 
counts the input_number of lines in the input file. Use argparse to handle the command-line arguments.
To run the script and count the input_number of lines in a file named input.txt and write the output to
 a file named output.txt'''
'''import argparse

par = argparse.ArgumentParser(description="Count the input_number of line in file and print the result in another file")
par.add_argument('input', help="open this file and read the input_number of file")
par.add_argument('output', help="print the result in this file ")
args = par.parse_args()


def read_write_files(input_file, output):
    count = 0
    with open(input_file, "r") as file:
        for line in file:
            count += 1
        # print(count)
    with open(output, "w") as output_file:
        output_file.writelines(str(count))


# read_write_files("sorted_list_of _string.txt","data.json")
read_write_files(args.input,args.output)'''
# Write a Python script that takes an optional verbose flag and a required string argument, and prints the
# string in uppercase if the verbose flag is set. Use argparse to handle the command-line arguments.
import argparse

parser = argparse.ArgumentParser(description="training  to argparse")
parser.add_argument("text",type=str,help="the string to be upper case")
parser.add_argument("-u","--uppercase",action="store_true",help="made the sting upper case if set")
args=parser.parse_args()
if args.uppercase:
    print(args.text.upper())
else:
    print(args.text.lower())
'''# parser.add_argument('count',type=int,help="count the input_number ")
# parser.add_argument('word',type=str,help="string to be reapeted")
# parser.add_argument('-n','--name',help="annonmues",default=" no name")
parser.add_argument("input_number", type=int, help='the input_number to be squre or cubed')
parser.add_argument("-p", "--power",type=int, default=2, choices=[2, 3], help='the power of numer')
args = parser.parse_args()
result = args.input_number ** args.power
print(f"{args.input_number} to power of {args.power} is {result} ")
# print("hello ",args.name)'''
'''
import argparse

parser = argparse.ArgumentParser(description="A script that calculates the square or cube of a input_number")
parser.add_argument("input_number", type=int, help="The input_number to be squared or cubed")
parser.add_argument("-p", "--power", type=int, default=2, choices=[2, 3], help="The power to raise the input_number to (2 for square, 3 for cube)")
args = parser.parse_args()

result = args.input_number ** args.power
print(f"{args.input_number} to the power of {args.power} is {result}")
'''