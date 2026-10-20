#avoid Race Condition - 1. Lock-Aquire()/Unlock-Release()

from threading import *
from time import sleep

mylock = Lock()

def task (mylock, msg):
    for i in range(5):
        print(msg)
    
    sleep(3)

t1=Thread(target=task, args=(mylock, 'Hello World'))
t2=Thread(target=task, args=(mylock, 'Welcome Here!'))

t1.start()
t2.start()

print("\n################################\n")


from threading import *
from time import sleep

mylock = Lock()

def task (mylock, msg):
    mylock.acquire()

    for i in range(5):
        print(msg)
    
    sleep(3)

    mylock.release()

t1=Thread(target=task, args=(mylock, 'Hello World'))
t2=Thread(target=task, args=(mylock, 'Welcome Here!'))

t1.start()
t2.start()

print("\n################################\n")


from threading import *
from time import sleep

lock = Lock()

class Bus:
    def __init__(self, name, available_seats, l):
        self.available_seats = available_seats
        self.name = name
        self.l = l

    def reserve(self, need_seats):
        self.l.acquire()

        print("Available seats are: ", self.available_seats)

        if self.available_seats >= need_seats:
            nm = current_thread().name

            print(f"{need_seats} are allocated to {nm}")

            self.available_seats -=need_seats
        else:
            print("Sorry! Seats atre not available.")

        self.l.release()

b1=Bus("Shyamoli Paribahan", 2, lock)

t1=Thread(target=b1.reserve, args=(1,), name="Yug")
t2=Thread(target=b1.reserve, args=(1,), name="Adi")

t1.start()
t2.start()

print("\n################################\n")


from threading import *
from time import sleep

lock = Lock()

class Bus:
    def __init__(self, name, available_seats, lock):
        self.available_seats = available_seats
        self.name = name
        self.lock = lock

    def reserve(self, need_seats):
        self.lock.acquire()
        print(self.lock)

        print("Available seats are: ", self.available_seats)

        if self.available_seats >= need_seats:
            nm = current_thread().name

            print(f"{need_seats} are allocated to {nm}")

            self.available_seats -=need_seats
        else:
            print("Sorry! Seats atre not available.")

        self.lock.release()

b1=Bus("Shyamoli Paribahan", 2, lock)

t1=Thread(target=b1.reserve, args=(1,), name="Yug")
t2=Thread(target=b1.reserve, args=(1,), name="Adi")

t1.start()
t2.start()