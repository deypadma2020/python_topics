import threading
from time import sleep

e = threading.Event()

def light_switch():
    while True:
        print("Light is green")
        e.set()
        sleep(5)

        print("Light is red")
        e.clear()
        sleep(5)
        e.set()

def traffic_message():
    e.wait()
    while e.is_set():
        print("You can go!")
        sleep(0.5)
        e.wait()

t1 = threading.Thread(target=light_switch)
t2 = threading.Thread(target=traffic_message)

t1.start()
t2.start()