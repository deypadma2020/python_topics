from threading import *
from time import sleep

rlock = RLock()

class Bus:
    def __init__(self, name, available_seats, rlock):
        self.available_seats = available_seats
        self.name = name
        self.rlock = rlock

    def reserve(self, need_seats):
        self.rlock.acquire()
        self.rlock.acquire()
        print(self.rlock)

        print("Available seats are: ", self.available_seats)

        if self.available_seats >= need_seats:
            nm = current_thread().name

            print(f"{need_seats} are allocated to {nm}")

            self.available_seats -=need_seats
        else:
            print("Sorry! Seats atre not available.")

        self.rlock.release()
        self.rlock.release()

b1=Bus("Shyamoli Paribahan", 2, rlock)

t1=Thread(target=b1.reserve, args=(1,), name="Yug")
t2=Thread(target=b1.reserve, args=(1,), name="Adi")

t1.start()
t2.start()