"""
Exercise 5: Synchronization

Description: Implement a counter that is incremented by multiple threads without data corruption using locks.

Steps:

Define class Counter that initializes a counter variable to 0, and initializes a lock.

Define a function called worker that accepts an integer argument increment, and a lock object lock. The worker
 function should acquire the lock,
 increment the counter variable by increment, print out the new value of the counter variable, and release the lock..

Create two threads, passing the worker function to both threads as well as the increment value of 1 for one thread and -1 for the other thread, and passing the same lock object to both threads.

"""
import threading
import time
from multiprocessing import Lock

#
class Counter:
    counter=0
    lock=Lock()
# counter = 0
# lock = Lock()


    def worker(self,increment, lock):
        Counter.counter
        lock.acquire()
        local_counter = Counter.counter + increment
        Counter.counter = local_counter
        print(Counter.counter)
        lock.release()

# lock=Counter.lock
'''c1=Counter()
c1.worker(10,Counter.lock)
c1.worker(10,Counter.lock)
c2=Counter()
c2.worker(10,Counter.lock)
c2.worker(10,Counter.lock)'''
c=Counter()
# worker=c.worker(10,c.lock)
thread1=threading.Thread(target=c.worker, kwargs={'increment':1,'lock':c.lock})
thread2=threading.Thread(target=c.worker, kwargs={'increment':-1,'lock':c.lock})

thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("final value",c.counter)