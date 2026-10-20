# daemon threads examples

from threading import *
from time import sleep

def display():
    for i in range(10):
        print("Teaching session", i)
        sleep(0.7)

display()

print("Exam time!")
print("Exam is over!")

print("\n################################\n")

from threading import *
from time import sleep

def display():
    for i in range(10):
        print("Teaching session", i)
        sleep(0.7)

t1 = Thread(target=display)

t1.start()

print("Exam time!")
print("Exam is over!")

print("\n################################\n")

from threading import *
from time import sleep

def display():
    for i in range(10):
        print("Teaching session", i)
        sleep(0.7)

t1 = Thread(target=display)
t1.daemon = True
t1.start()

print("Exam time!")
print("Exam is over!")

print("\n################################\n")

from threading import *
from time import sleep

def display():
    for i in range(10):
        print("Teaching session", i)
        sleep(0.7)

t1 = Thread(target=display)
t1.daemon = True
t1.start()
sleep(3)
print("Exam time!")
print("Exam is over!")

print("\n################################\n")

from threading import *
from time import sleep

def syntax_highlighting():
    for i in range(10):
        print("Syntax highlighting")
        sleep(1)

t1 = Thread(target=syntax_highlighting)
t1.daemon = True
t1.start()
sleep(3)
print("Close the application!")
