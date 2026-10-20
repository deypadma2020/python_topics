# 1.Timer Object

import threading

def task():
    for i in range(5):
        print("hello")

timer = threading.Timer(10, task)
timer.start()

for i in range(5):
    print(threading.current_thread().name)