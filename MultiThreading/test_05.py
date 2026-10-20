from threading import Thread

class Example:
    def display(self,n):
        for i in range(n):
            print("Hello World")

e1 = Example()
t1 = Thread(target=e1.display, args=(4,))
t1.start()

for i in range(5):
    print("Welcome!")

print("\n####################\n")

from threading import Thread

class Example:
    @classmethod
    def display(self,n):
        for i in range(n):
            print("Hello World")

t1 = Thread(target=Example.display, args=(4,))
t1.start()

for i in range(5):
    print("Welcome!")

print("\n####################\n")

from threading import Thread

class Example:
    @staticmethod
    def display(n):
        for i in range(n):
            print("Hello World")

t1 = Thread(target=Example.display, args=(4,))
t1.start()

for i in range(5):
    print("Welcome!")