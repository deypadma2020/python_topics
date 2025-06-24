# Exception
from threading import *
from time import sleep

def display():
    for i in range(4):
        sleep(2)
        print("hello: "+10)

def show():
    for i in range(4):
        print("hello")
        sleep(0.5)

t1=Thread(target=display)
t2=Thread(target=show)

t1.start()  # run() -> display()
t2.start()

t1.join()
t2.join()

for i in range(4):
    print("Bye!!!")

print("\n################################\n")

# What happens for exception in thread?
# - the interpreter calls threading.excepthook() with one argument, 
#   i.e. named tuple with 4 arguments

#     1. the exception class
#     2. exception instance/value 
#     3. a traceback object
#     4. Thread name

#   * For main thread -> sys.excepthook
#   * For created thread -> threading.excepthook --> sys.excepthook

print("\n################################\n")

import threading
from time import sleep

def custom_hook(args):
    print("Exception occured in the thread...")
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])

def display():
    for i in range(4):
        sleep(2)
        print("hello: "+10)

def show():
    for i in range(4):
        print("hello")
        sleep(0.5)

threading.excepthook=custom_hook

t1=threading.Thread(target=display)
t2=threading.Thread(target=show)

t1.start()  # run() -> display()
t2.start()

t1.join()
t2.join()

for i in range(4):
    print("Bye!!!")