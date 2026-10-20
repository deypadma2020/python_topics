'''
1. is_alive() - checks thread is running or not
2. main_thread() - returns main threads details
3. active_count() - number of running threads
4. enumerate() - list of all running threads
5. get_native_id() - know native id of thread
'''

import os
from threading import Thread

def display():
    for i in range(4):
        print("Hello World!")

def show():
    for i in range(3):
        print("Welcome!")

t1 = Thread(target=display)
print("before: ", t1.is_alive())
t1.start()
print("After",t1.is_alive())


print("\n###############################\n")

import os
from threading import Thread, main_thread

def display():
    print("main thread details: ", main_thread())
    for i in range(4):
        print("Hello World!")

def show():
    for i in range(3):
        print("Welcome!")

t1 = Thread(target=display)
print("before: ", t1.is_alive())
t1.start()
print("After",t1.is_alive())

print("\n###############################\n")

import os
from threading import Thread, main_thread, active_count

def display():
    print("main thread details: ", main_thread())
    for i in range(4):
        print("Hello World!")

def show():
    for i in range(3):
        print("Welcome!")

t1 = Thread(target=display)
print("before: ", t1.is_alive())
t1.start()
print("number of threads: ", active_count())
print("After",t1.is_alive())

print("\n###############################\n")

import os
from threading import Thread, main_thread, active_count, enumerate

def display():
    print("main thread details: ", main_thread())
    for i in range(4):
        print("Hello World!")

def show():
    for i in range(3):
        print("Welcome!")

t1 = Thread(target=display)
print("before: ", t1.is_alive())
t1.start()
print("number of threads: ", enumerate())
print("After",t1.is_alive())

print("\n###############################\n")

import os
from threading import Thread, main_thread, enumerate, get_native_id

def display():
    print("native id of t1: ", get_native_id())
    print("main thread details: ", main_thread())
    for i in range(4):
        print("Hello World!")

def show():
    for i in range(3):
        print("Welcome!")

t1 = Thread(target=display)
print("before: ", t1.is_alive())
t1.start()
print("native_id of main thread: ", get_native_id())
print("number of threads: ", enumerate())
print("After",t1.is_alive())