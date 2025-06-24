#   queue data structure(FIFO - first in first out)


# queue.Queue() class

# Syntax: -
    # import queue
    # my_que = queue.Queue(maxsize=optional aregument)


# 1. put(item, block = True): -
#     this method used to insert elements into queue.

# 2. get(): -
#     this method is used to delete elements from queue.

# Benefits: - 
    # 1. Thread safe: - No Race Condition
    # 2. implements all the required locking semantics


from time import sleep
from threading import Thread
from queue import Queue

my_que = Queue()

def producer(my_que):
    print("producer: running")
    n = int(input("Enter number of students: "))

    for i in range(n):
        marks = float(input("Enter marks: "))
        my_que.put(marks)
    
    my_que.put(None)

    print("producer: end")

def consumer(my_que):
    print("consumer: running")

    while True:
        item = my_que.get()
        if item is None:
            break

        print(f"Got {item}")

    print("consumer: end")

t1 = Thread(target=producer, args=(my_que,))
t2 = Thread(target=consumer, args=(my_que,))

t1.start()
t2.start()