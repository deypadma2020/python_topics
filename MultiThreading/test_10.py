#using Multithreading

from threading import Thread
import time

def square(num):
    print("Finding square...")
    time.sleep(1)
    print(f"square of {num} is: {num**2}")

def cube(num):
    print("Finding cube...")
    time.sleep(1)
    print(f"cube of {num} is: {num**3}" )

begin = time.time()

t1=Thread(target=square,args=(3,))
t2=Thread(target=cube,args=(3,))

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print("Total time taken: ", end - begin)


print("\n################################\n")

# without using multithreading

from threading import Thread
import time

def square(num):
    print("Finding square...")
    time.sleep(1)
    print(f"square of {num} is: {num**2}")

def cube(num):
    print("Finding cube...")
    time.sleep(1)
    print(f"cube of {num} is: {num**3}" )

begin = time.time()

square(3)
cube(3)

end = time.time()

print("Total time taken: ", end - begin)