'''
Task 1 - Simple To-Do List Manager
Create a To-Do List Manager that manages the tasks you need to perform. This manager should support the following operations

Add a task: adds a task to the list
Remove a task: removes a task from the list
Modify a task: Modifies an already inserted task
Your program should provide the user at the beginning with a list of operation to choose from. Make sure that your program does not crash when a user enters a bad choice!

When a user enters the option - you need to print current status of the to do list and the new list after an operation is performed.
'''
ListTask = []
print("Press [1] To Add a task\n",
      "Press[2] To removes a task from the list\n"
      "Press [3] To  Modifies a task from a list\n"
      "Press [exit] To exit from Program ")

while True:
    choose = input("Enter your choice")
    if choose == '1':
        print("The list of Task : ", ListTask)
        enterTask = input("Write the task please")
        ListTask.append(enterTask)
        print("The task added successfully the new list is : ", ListTask)
    elif choose == '2':
        print("The list of Task : ", ListTask)
        removeTask = input("Write the task you want to remove it please")
        if removeTask in ListTask:
            ListTask.remove(removeTask)
            print("The task remove successfully the new list is : ", ListTask)
        else:
            print("Sorry the task is not found!")


    elif choose == '3':
        print("The list of Task : ", ListTask)
        modifayaTask = input("Please enter the task you want to modify it")
        if modifayaTask in ListTask:
            ListTask[modifayaTask] = input("Enter the new task: ")
            print("The task modify successfully  the new list is : ", ListTask)
        else:
            print("Sorry the task is not found!")
    elif choose == 'exit':
        print("Good bya ^_^ ")
        break
    else:
        print("Invalid option please enter from the list ")
