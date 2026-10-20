### Thread Communication
    # 1. by creating event object
    # 2. by creating condition object
    # 3. by using queue module 

# Using Event Object: -
    # 1. We have to create an event object.
    # 2. create two threads which will communicate.
    # 3. put t2 thread in waiting by using wait()
    # 4. use set() method in/after t1 threads code.

# set(): -
    # 1. set the internal flag to true.
    # 2. if flag is True, waiting thraed is awakened. 

# reset(): -
    # 1. reset the internal flag to False. 
    # 2. other thread will wait() again.

# is_set(): -
    # 1. Return True if and only if the internal flag is True.
    #     ex: - if event.is_set():
    #                 do somthing...

# wait([timeout]): -
    # 1. Calling this function keep other thread on wait untill flag is set to True.

import threading
import time

e = threading.Event() # step-01

def task():
    print("game is started")
    time.sleep(5)
    e.set()

def end():
    e.wait()
    if e.is_set():
        print("code for destroying session")

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=end)

t1.start()
t2.start()