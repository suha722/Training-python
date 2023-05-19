# Summing numbers with a loop: Write a program that asks the user to enter a input_number,
# then uses a loop to add_book up all the numbers from 1 to that input_number. The program should print the sum
'''num=input('Hi sir can enter the input_number to sum it')
summ=0
try:
    num=int(num)
    for input_number in range(num+1):
        summ+=input_number
    print('The sum is :',summ)
except ValueError:
    print('Please enter input_number not other thing')

'''
# Counting the input_number of vowels in a string with a loop: Write a program that asks the user to enter a string,
# then uses a loop to count the input_number of vowels (a, e, i, o, u) in the string. The program should print
# the input_number of vowels.
'''vowels=['A','a','O','o','u','U','I','i','e','E']
Enterstring=input('Hi enter the string you want count the input_number of vowels in it :')
count=0
for i in Enterstring:
    if i in vowels:
        count+=1
print(count)'''
# Reversing a string with a loop: Write a program that asks the user to enter a string, then uses a loop to
# print the string in reverse order. The program should print the reversed string
'''Enterstring=input('Hi enter the string you want reverse it t :')
n=len(Enterstring)
for i in range(1,n+1,):
    print(Enterstring[-i],end='')'''
# Finding the largest input_number in a list with a loop: Write a program that creates a list of numbers, then uses
# a loop to find the largest input_number in the list. The program should print the largest input_number.#
'''list=[22,3,4,5,7,9,77,66,54,32,5]
largest=list[0]
for i in list:
    if i>largest:
        largest=i
print('The largest input_number in the list is :',largest)'''
# Counting the input_number of words in a string with a loop: Write a program that asks the user to enter a sentence,
# then uses a loop to count the input_number of words in the sentence. The program should print the input_number of words.
Enterstring = input('Hi enter the string you want to count the words in it :')
count_word = 0
# num=len(Enterstring.split())
# print(num)
for i in Enterstring.split(' '):
    if len(i) >= 2:
        count_word += 1
print(count_word)
# Printing a multiplication table with nested loops: Write a program that uses nested loops to print a
# multiplication table for the numbers 1 to 10. The program should output each row on a new line.
'''print('The multiplication table is :')
for i in range(1,11):
    for j in range(11):
        print(i,'X',j,'=',i*j)
    print('___________________________________')'''
