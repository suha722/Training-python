"""
Exercise 6: Deadlock

Description: Create a deadlock between two threads by acquiring locks in the wrong order.

Steps:

Define a class called Resource that has two instance variables, lock1 and lock2, which are both instances of the threading.Lock class. This will allow us to simulate two resources that can be locked and unlocked by multiple threads.

Define a method called do_something on the Resource class that acquires lock1 first and then lock2 second, and prints out a message indicating that both locks have been acquired.

Define two worker functions, worker1 and worker2, that will be executed by two different threads. worker1 simply calls do_something on the Resource object that is passed to it as an argument, while worker2 acquires lock2 first and then lock1 second, and prints out a message indicating that both locks have been acquired.

Create a Resource object and two threads, passing the Resource object to both threads as an argument.

Start both threads.


"""

import threading


class Resource:
    lock1=threading.Lock()
    lock2=threading.Lock()
    def do_somthing(self):
        self.lock1.acquire()
        self.lock2.acquire()
        print("indicating that both locks have been acquired.")



def worker1(res):
    res.do_somthing()
def worker2(res):
    res.lock2.acquire()
    res.lock2.acquire()
    print("indicating that both locks have been acquired.")
res=Resource()
thread1=threading.Thread(target=worker1,args=res)
thread2=threading.Thread(target=worker2,args=res)
thread1.start()
thread2.start()
thread1.join()
thread2.join()

