"""
Exercise 1: Simple Thread Creation

Description: Create a simple thread that prints out a message.


"""
import queue
import threading
from concurrent.futures import ThreadPoolExecutor

'''import queue
import threading
import time as t
import multiprocessing
from random import random


def hello_word():
    print("Hello World!\n")
    print("thread end !\n")



start = t.perf_counter()

thread = threading.Thread(target=hello_word)
thread.start()
thread.join()
end = t.perf_counter()
print(f"Finished  in time {round(end - start, 9)}")'''

"""
Exercise 2: Multiple Thread Creation

Description: Create multiple threads that print out a message.

"""
'''def hello_word():
    print("Hello World!",p)


start = t.perf_counter()
thread_list=[]
for _ in range(10):
    thread=threading.Thread(target=hello_word)
    thread_list.append(thread)
    thread.start()
for th in thread_list:
    th.join()
end = t.perf_counter()
print(f"Finished  in time {round(end - start, 9)}")
from multiprocessing import Process ,current_process,Value,Lock
'''
"""
Exercise 3: Producer-Consumer Problem

Description: Implement a producer-consumer problem using threads and a shared queue.

"""
'''from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Thread,current_thread
qu=queue.Queue()

def consumer(queue):
    # print('Consumer: Running')
    #
    # # consume items
    while True:
        # get a unit of work
        item = queue.get()
        # check for stop
        if item is None:
            break
        # report
        return ( f'>consumer item ')

def producer(queue):

    for i in range(5):
        item = (i, 10)
        # add to the queue
        queue.put(item)
        # report progress
        return( f'>producer item')
    # signal that there are no further items
    # queue.put(None)
    # print(f"{item}")
    # print(f"Produced Item {current_thread().name}")


# create a producer thread
count=0
with ThreadPoolExecutor() as executor:
#
    f2 = [executor.submit(producer,qu)]
    f1=[executor.submit(consumer, qu)]
    while count!=10:
        for f in as_completed(f1):
            print(f.result(),count)
        for f in as_completed(f2):
            print(f.result(),count)
        count+=1
'''


"""
Exercise 4: Thread Pool

Description: Use a thread pool to process a list of tasks. Check how to use
 concurrent.futures to create a pool of executors.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed


def taskstart(num):
    return ("Processing task",num)
def taskcomplite(num):
    return ("Completed task",num )
tasknumber=[1,2,3,4,5]
with ThreadPoolExecutor() as executor:
    f1=[executor.submit(taskstart,t) for t in tasknumber]
    f2 = [executor.submit(taskcomplite, t) for t in tasknumber]
    for f in as_completed(f1):
        print(f.result())
    for f in as_completed(f2):
        print(f.result())
# another solution:
def task(num):
    print(f"processing task{num}")
    print(f"complited task{num}")
with ThreadPoolExecutor() as executor:
    for i in range(5):
        f=executor.submit(task,i)


