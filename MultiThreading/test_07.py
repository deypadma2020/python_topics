from threading import Thread

def display():
    for i in range(4):
        print("Hello World!")

def show():
    for i in range(3):
        print("Welcome!")

t1 = Thread(target=display)
t2 = Thread(target=show)

print(t1.name)
print(t2.name)

print("\n############################\n")

from threading import Thread

def display():
    for i in range(4):
        print("Hello World!")

def show():
    for i in range(3):
        print("Welcome!")

t1 = Thread(target=display)
t2 = Thread(target=show)

print(t1.getName())
print(t2.getName())

print("\n############################\n")

from threading import Thread

def display():
    for i in range(4):
        print("Hello World!")

def show():
    for i in range(3):
        print("Welcome!")

t1 = Thread(target=display)
t2 = Thread(target=show)

t1.name = "test_thread-1"
t2.name = "test_thread-2"

print(t1.name)
print(t2.name)

print("\n############################\n")

from threading import Thread, current_thread

def display():
    for i in range(4):
        print("Hello World!")

def show():
    for i in range(3):
        print("Welcome!")

t1 = Thread(target=display)
t2 = Thread(target=show)

t1.name = "test_thread-1"
t2.setName("test_thread-2")

print(t1.name)
print(t2.name)

print(current_thread().name)

current_thread().name = "MasterThread"
print(current_thread().name)


print("\n###############################\n")


## Thread Identifier - Process(ident) | Native identifier - Operating System(native_id)
## PID - OS Module: - getpid()

import os
from threading import Thread

def display():
    for i in range(4):
        print("Hello World!")

def show():
    for i in range(3):
        print("Welcome!")

t1 = Thread(target=display)
t2 = Thread(target=show)

t1.start()
t2.start()

print("ident - ", t1.ident)
print("native_id - ", t2.native_id)
print(f"pid - {os.getpid()}")