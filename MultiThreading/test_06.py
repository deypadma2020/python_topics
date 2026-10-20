# from threading import Thread

# def display():
#     a=10
#     b=20
#     return a+b

# t1 = Thread(target=display)
# print(t1.start()) # -> None

# print("\n###############################\n")

from time import sleep
from threading import Thread

videos = ['OOP Syllabus', 'Constructor', 'Destructor', 'File Handling']

class MyClass(Thread):
    def __init__(self, val):
        print("Constructor called!")
        self.kid=val
        Thread.__init__(self)

    def compression(self):
        print("Video compression code!")

    def run(self):
        a=10
        b=20
        sum = a+b
        self.compression()
        if self.kid:
            print("Suitable for kids")
        for video in videos:
            print(f"{video} started uploading...")
            sleep(1)
            print(f"{video} uploaded.")
        self.temp =  sum

t1 = MyClass(True)
t1.start()

# sleep(10)
t1.join()

print(f"The result is: {t1.temp}")

for i in range(4):
    sleep(0.5)
    print("Checking copyrights")


print("\n###############################\n")


# from time import sleep

# videos = ['OOP Syllabus', 'Constructor', 'Destructor', 'File Handling']

# def upload(videos):
#     print(f"{videos} started uploading...")
#     sleep(3)
#     print(f"{videos} uploaded.")

# for i in range(4):
#     sleep(0.5)
#     print("Checking copyrights")

# print("\n###############################\n")

# from time import sleep
# from threading import Thread

# videos = ['OOP Syllabus', 'Constructor', 'Destructor', 'File Handling']

# class MyClass(Thread):
#     def run(self):
#         for video in videos:
#             print(f"{video} started uploading...")
#             sleep(3)
#             print(f"{video} uploaded.")

# t1 = MyClass()
# t1.start()

# for i in range(4):
#     sleep(0.5)
#     print("Checking copyrights")
    
# print("\n###############################\n")

# from time import sleep
# from threading import Thread

# videos = ['OOP Syllabus', 'Constructor', 'Destructor', 'File Handling']

# class MyClass(Thread):
#     def __init__(self):
#         print("Constructor called")
#         Thread.__init__(self)
#     def run(self):
#         for video in videos:
#             print(f"{video} started uploading...")
#             sleep(3)
#             print(f"{video} uploaded.")

# t1 = MyClass()
# t1.start()

# for i in range(4):
#     sleep(0.5)
#     print("Checking copyrights")

# print("\n###############################\n")

from time import sleep
from threading import Thread

videos = ['OOP Syllabus', 'Constructor', 'Destructor', 'File Handling']

class MyClass(Thread):
    def __init__(self, val):
        print("Constructor called!")
        self.kid=val
        Thread.__init__(self)

    def compression(self):
        print("Video compression code!")

    def run(self):
        self.compression()
        if self.kid:
            print("Suitable for kids")
        for video in videos:
            print(f"{video} started uploading...")
            sleep(3)
            print(f"{video} uploaded.")

t1 = MyClass(True)
t1.start()

for i in range(4):
    sleep(0.5)
    print("Checking copyrights")

print("\n################################\n")

from threading import Thread

def display():
    for i in range(5):
        '''
        Threading module: - 
        class Thread:
            def run(self):
                display()
        '''
        print("Hello World")

t1 = Thread(target=display)
t1.start()

print("\n################################\n")

class MyThread(Thread): 
    '''
    my own custom class inherited by main Thread class - this method is called as method overwriting
    '''
    def run(self):
        #code
        print("Hello World")

t1 = MyThread
t1.start()