'''
Task 2 - Grocery Store
Functional Requirements

The user should be able to add_book items to the grocery list.
The user should be able to remove items from the grocery list.
The user should be able to view the current grocery list.
The user should be able to calculate the total cost of the items on the grocery list.
The user should be able to quit the program.
Non-functional Requirements

The program should display a menu of options to the user.
The program should validate user input and handle errors gracefully.
The program should display clear, easy-to-understand messages to the user.
The program should be well-organized and easy to read.
The program should be well-documented with comments where appropriate.
These requirements should be used to guide the design and implementation of the Grocery List Manager project, ensuring that it meets the needs of the user and is of high quality.

'''
Grocery_list=['potato',5,'banana',7,'tomato',8,'lettuce',4]
grocery=[]
totalcost=0
print("Hi how are you what you want to add_book in the list")
print("______________________________________________________\n"
      "press[1]to add_book Potato price is 5 \n"
      "press[2]to add_book Banana price is : 7\n"
      "press[3]to add_book Tomato price is :8\n "
      "press[4]to add_book lettuce price is :4\n"
      "press[5] to remove item from your list\n"
      "press[6] to find the total cost\n"
      "press[7]to exit from program\n"
      "_______________________________________________________\n"
      )
while True:
    choose=input("enter the choose ")
    if choose=='1':
        grocery.append(Grocery_list[0])
    elif choose=='2':
        grocery.append(Grocery_list[2])
    elif choose=='3':
        grocery.append(Grocery_list[4])
    elif choose=='4':
        grocery.append(Grocery_list[6])
    elif choose=='5':
        removeitem=input("Enter the item you want to remove")
        if removeitem in grocery:
            grocery.remove(removeitem)

        else:
            print("Sorry the item not found!")
    elif choose=='6':
        if 'potato' in grocery:
            totalcost+=Grocery_list[1]
        if 'banana' in grocery:
            totalcost += Grocery_list[3]
        if 'tomato' in grocery:
            totalcost += Grocery_list[5]
        if 'lettuce' in grocery:
            totalcost += Grocery_list[7]
        print("The total cost is ",totalcost,"$")
    elif choose=='7':
            print("Good bya!")
            break
    else:
        print("Invailed option!")
    print("The grocery list is ",grocery)
    print("*************************************************")
