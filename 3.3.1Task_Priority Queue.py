"""

Task - Implementing a Priority Queue Data Structure
Project Description:

In this project, we will be implementing a priority queue data structure in Python without using classes. A priority queue is a queue data structure that prioritizes elements according to their priority value.

Here are the main steps for implementing the project:

Create an empty list to represent the priority queue.
Implement the enqueue function to add_book elements to the priority queue according to their priority value.
Implement the dequeue function to remove the element with the highest priority value from the priority queue.
Implement the is_empty function to check if the priority queue is empty.

"""
queue_size = 100


def insert_in_queue(queue_list, element, priority):
    """
    this function  add_book element to the queue
    :param queue_list: list as a queue
    :param element: the first element in tuple
    :param priority: the priority in the list
    :return: add_book element to the  queue
    """
    if queue_size < len(queue_list):
        print("The queue is full!")
    else:
        # list=[(element,priority)]
        value = (element, priority)
        queue_list.append(value)
    # return queue_list


def delete_from_queue(queue_list):
    try:
        item_delete = 0
        if not queue_list:
            return "queue is empty!"
        else:

            max_value = 0
            for item in range(len(queue_list)):
                if queue_list[item][1] > queue_list[max_value][1]:
                    max_value = item

            item_delete = queue_list[max_value]
            del queue_list[max_value]
            return item_delete
    except IndexError:
        print()


def is_empty(queue_list):
    return len(queue_list) == 0


# Create an empty list to represent the queue
queue_list = []
priority_queue = []
insert_in_queue(queue_list, "task2", 1)
insert_in_queue(queue_list, "task 3", 3)
insert_in_queue(queue_list, "task 4", 4)
print("The queue before priority is :\t", queue_list)
while not is_empty(queue_list):
    priority_queue.append(delete_from_queue(queue_list))
print("The queue after priority :\t ", priority_queue)
print("The queue is empty?:", is_empty(queue_list))

