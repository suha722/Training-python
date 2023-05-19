# implement normal queue
queue_size = 20


def insert_in_queue(queue_list, element):
    if queue_size < len(queue_list):
        print("The queue is full!")
    else:
        queue_list.append(element)
    return queue_list


def delete_from_queue(queue_list):
    try:
        item_delete = 0
        if not queue_list:
            return "queue is empty!"
        else:
            item_delete = queue_list.pop(0)
            return item_delete
    except IndexError:
        print()


def is_empty(queue_list):
    return len(queue_list) == 0


queue_list = []
print(delete_from_queue(queue_list))
insert_in_queue(queue_list, "2")
print(delete_from_queue(queue_list))


insert_in_queue(queue_list, "3")
insert_in_queue(queue_list, "4")
print(queue_list)
while not is_empty(queue_list):
    print(delete_from_queue(queue_list))

print(is_empty(queue_list))
# implement queue using library
from queue import Queue
que=Queue(maxsize=5)
print("the size before adding in queue: \t",que.qsize())
while que.full()==False:
    que.put(("task1",1))
    que.put(("task2",2))
    que.put(("task3",3))
    que.put(("task4",4))
    que.put(("task4",5))
else:
    print("The queue is full!!")
    print(que.qsize())
while not que.empty():
    print(que.get())

