from threading import Thread

def display(n, msg):
    for i in range(n):
        print(msg)

t1 = Thread(target=display, kwargs={'n': 4, 'msg': "Hello World"})

t1.start()

for i in range(4):
    print("Welcome")

print("\n###################################\n")

from threading import Thread

def display(n, msg):
    for i in range(n):
        print(msg)

t1 = Thread(target=display, args=(4, "Hello World"))

t1.start()

for i in range(4):
    print("Welcome")

print("\n###################################\n")

from threading import Thread

def display(n, msg):
    for i in range(n):
        print("Hello")

t1 = Thread(target=display, args=(4,))

t1.start()

for i in range(4):
    print("Welcome")

print("\n###################################\n")

from threading import Thread, current_thread

def display(n, msg):
    print("t1 thread details: ", current_thread())
    for i in range(n):
        print(msg)

t1 = Thread(target=display, kwargs={'n': 4, 'msg': "Hello World"})

t1.start()

for i in range(4):
    print("Welcome")

print("\n###################################\n")

from threading import Thread, current_thread

def display(n, msg):
    print("t1 thread details: ", current_thread().name)
    for i in range(n):
        print(msg)

t1 = Thread(target=display, kwargs={'n': 4, 'msg': "Hello World"})

t1.start()

for i in range(4):
    print("Welcome")

print("\n###################################\n")

from threading import Thread, current_thread

def display(n, msg):
    print("t1 thread details: ", current_thread().ident)
    for i in range(n):
        print(msg)

t1 = Thread(target=display, kwargs={'n': 4, 'msg': "Hello World"})

t1.start()

for i in range(4):
    print("Welcome")