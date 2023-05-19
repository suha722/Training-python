#1) #Write a Python program to create a list of numbers from 1 to 10 and print only the even numbers.
'''list=[]
for i in range(1,11):
    list.append(i)
     # print(list)
for j in list:
    if j%2==0:
        print(j)'''
###############
#2)Write a Python program to remove duplicates from a list.
'''listduplicate=[1,2,3,3,4,5]
newlist=[]
for num in listduplicate:
    if num not in newlist:
        newlist.append(num)
print(newlist)'''
#############
#3)write a Python program to find the largest and smallest numbers in a list.
largsmalllist=[1,3,4,4,7,8]
'''print("The max input_number in the list is: ",max(largsmalllist))
   print("The smallest input_number in the list is: ",min(largsmalllist))
'''
#4)Write a Python program to concatenate two lists.
'''list1=[1,3,4,5]
list2=[3,5,6]
newlist=list1+list2
print(newlist)
list1.append(list2)
list1.extend(list2)
print(list1)'''
#5)Write a Python program to find the second largest input_number in a list.
'''list=[7,2,3,4,5,6]
list.sort()
print(list[-2])'''
#6)Write a Python program to split a list into two parts, where the first part contains the
# first three elements and the second part contains the remaining elements.
'''list=[1,2,4,5,7,89,9]
print("first part ",list[:3],"\n The second part: ",list[3::])'''
# 7)#Write a Python program to find the sum of all the numbers in a list.
'''list=[1,2,4,5,6]
summ=0
print(sum(list))
for i in list:
    summ+=i
print(summ)'''
