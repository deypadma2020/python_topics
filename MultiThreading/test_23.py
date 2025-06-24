### Threads are two types - 
# (1) Daemon Threads 
# (2) Non-Demon Threads (program will not terminate untill all non-deamon threads gets completed)

# * IDLE app: -

    # Thread 1: - Main Thread - Non-Demon Threads
    # Thread 2: - Thread for interactive shell - Non-Demon Threads
    # Thread 3: - Thread for Editor - Non-Demon Threads
    # Thread 4: - Thread for python interpreter - Non-Demon Threads
    # Thread 5: - Thread for text highlighting - Demon Threads 
    # Thread 6: - Thread for memory management - Demon Threads 

# t1 = Thread(task=target)
# here, instance variables: -
#     1. name
#     2. ident 
#     3. Native id 
#     4. daemon (boolian value; if True then Daemon thread, else Non-Daemon thread)
# t1.daemon = True

#  checking daemon nature of main thread - Non-Daemon thread

from threading import *
obj = current_thread()
print("daemon nature of main thread", obj.daemon)

print("\n###############################\n")

from threading import *
def display():
    print("This is display function")

t1 = Thread(target= display)    
print("daemon nature of main thread before", t1.daemon)
t1.daemon = True
print("daemon nature of main thread after", t1.daemon)
t1.start()


print("\n###############################\n")

from threading import *
def display():
    print("This is display function")

t1 = Thread(target= display)    
print("daemon nature of main thread before", t1.daemon)

print("daemon nature of main thread after", t1.daemon)
t1.start()

# t1.daemon = True

print("\n###############################\n")

from threading import *
def display():
    print("This is display function")

t1 = Thread(target= display)    
print("daemon nature of main thread before", t1.daemon)
t1.setDaemon = True
print("daemon nature of main thread after", t1.daemon)
t1.start()

print("This is main Thread")

print("\n###############################\n")

from threading import *

def demo():
    print("Something...")

def display():
    print("This is display function")
    t2 = Thread(target = demo)
    print("daemon nature of t2: ", t2.daemon)

t1 = Thread(target= display)    
print("daemon nature of main thread before", t1.daemon)
# t1.daemon = True
print("daemon nature of main thread after", t1.daemon)
t1.start()

print("This is main Thread")