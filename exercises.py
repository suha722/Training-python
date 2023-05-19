# #Write a program to generate the Fibonacci sequence up to a given input_number.
'''fterm=int(input("plz enter the # of terms u want"))
n1=0
n2=1
count=0
if fterm<0:
    print("plz enter positive input_number ._.")
elif fterm==1:
    print("the Fibonacci of terms:",fterm)
    print(n1)
else:
    while count<fterm:
        print(n1)
        f_nth=n1+n2
        n1=n2
        n2=f_nth
        count+=1'''
# #2Write a program to find the factorial of a given input_number.
'''fact=int(input("enter the input_number u want to find factorial: "))
f=1
i=1
if fact<0:
    print("plz enter positive input_number ^_^")
elif fact==1:
    print("the factorial of",fact ,"is : ",f)
else :
    for i in range(1,fact+1):
        f=f*i
    print("The factorial of ",fact ," is:",f)'''
#Write a program to find the most common character in a string
'''from collections import Counter
def mostcommon(str1):
        temp=Counter(str1)
        most=max(temp,key=temp.get)
        minn=min(temp,key=temp.get)
        return (most,minn)
str1="hello word"
print("orginal string ",str1)
result=mostcommon(str1)
print("the most common character is ",result[0])
print("the min common character is ",result[1])
#Write a program to sort a list of strings by the length of each string.
def sorting(lst):
    ls2=sorted(lst,key=len)
    return ls2
lst1=["suha","ibrahim","waleed","sam"]
print(sorting(lst1))'''
#Write a program to remove all vowels from a string.
'''def removevowels(str1):
    vowel=["a","e","o","i","u","A","U","O","I","E"]
    str2=""
    for i in str1:
        if i not in vowel:
            str2=str2+i
    return str2
str=" suha"
print(removevowels(str))'''
# #Write a program to find the key with the maximum value in a dictionary.
'''
dic={"suha":12 ,"Ibrahim":123}
maxvalu=max(zip(dic.values(),dic.keys()))[1]
print(maxvalu)
#Write a program to count the frequency of words in a given string and store the results in a dictionary.
given_string=input("enter the string")
list1=[]
list1=given_string.split(" ")
countword=[list1.count(p) for p in list1]
dictionary=dict(zip(list1,countword))
print(dictionary)'''
