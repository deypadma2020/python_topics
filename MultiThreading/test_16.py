from threading import *
import time

obj=Semaphore()

def display(name):
    obj.acquire()

    for i in range(5):
        print('Hello')
        print(name)
        time.sleep(0.5)

    obj.release()


t1 = Thread(target=display, args=('Thread-1',))
t2 = Thread(target=display, args=('Thread-2',))
t3 = Thread(target=display, args=('Thread-3',))
t4 = Thread(target=display, args=('Thread-4',))
t5 = Thread(target=display, args=('Thread-5',))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

print("\n################################\n")

from threading import *
import time

obj=Semaphore()

def display(name):
    obj.acquire()
    obj.acquire()

    for i in range(5):
        print('Hello')
        print(name)
        time.sleep(0.5)

    obj.release()
    obj.release()


t1 = Thread(target=display, args=('Thread-1',))
t2 = Thread(target=display, args=('Thread-2',))
t3 = Thread(target=display, args=('Thread-3',))
t4 = Thread(target=display, args=('Thread-4',))
t5 = Thread(target=display, args=('Thread-5',))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

print("\n################################\n")

# this is not safe
from threading import *
import time

obj=Semaphore()

def display(name):
    obj.acquire()
    

    for i in range(5):
        print('Hello')
        print(name)
        time.sleep(0.5)

    obj.release()
    obj.release()


t1 = Thread(target=display, args=('Thread-1',))
t2 = Thread(target=display, args=('Thread-2',))
t3 = Thread(target=display, args=('Thread-3',))
t4 = Thread(target=display, args=('Thread-4',))
t5 = Thread(target=display, args=('Thread-5',))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

print("\n################################\n")

# thy use BoundedSemaphore
from threading import *
import time

obj=BoundedSemaphore()

def display(name):
    obj.acquire()
    obj.acquire()

    for i in range(5):
        print('Hello')
        print(name)
        time.sleep(0.5)

    obj.release()
    obj.release()


t1 = Thread(target=display, args=('Thread-1',))
t2 = Thread(target=display, args=('Thread-2',))
t3 = Thread(target=display, args=('Thread-3',))
t4 = Thread(target=display, args=('Thread-4',))
t5 = Thread(target=display, args=('Thread-5',))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

