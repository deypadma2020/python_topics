# Join method

from threading import Thread
from time import sleep

def upload():
    print("Uploading starts...")
    sleep(3)
    print("Video uploaded")

def notification():
    print("Sending notification to subscribers...")


t1 = Thread(target=upload)
t2 = Thread(target=notification)

t1.start()
t1.join()
t2.start()

for i in range(4):
    print("hello")

print("\n################################\n")

from threading import Thread
from time import sleep

def upload():
    print("Uploading starts...")
    sleep(3)
    print("Video uploaded")

def notification():
    print("Sending notification to subscribers...")


t1 = Thread(target=upload)
t2 = Thread(target=notification)

t1.start()
t1.join()
t2.start()
t2.join()

for i in range(4):
    print("hello")

print("\n################################\n")

from threading import Thread
from time import sleep

def upload():
    print("Uploading starts...")
    sleep(3)
    print("Video uploaded")

def notification():
    print("Sending notification to subscribers...")


t1 = Thread(target=upload)
t2 = Thread(target=notification)

t1.start()
# t1.join()
t2.start()
t2.join()

for i in range(4):
    print("hello")

