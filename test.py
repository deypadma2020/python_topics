# import sys

# def format_traceback(exc_type, exc_value, exc_traceback):
#     print("Something went wrong")
#     print(exc_type)
#     print(exc_value)
#     print(list(exc_traceback))


# sys.excepthook = format_traceback
# def display():
#     print(1+"hello")

# display()






# #does exception handled by multithreading?

# import threading
# from threading import *
# from time import sleep

# def custom_hook(args):
#     print("Exception occured in thread")
#     print(args[0])
#     print(args[1])
#     print(args[2])
#     print(args[3])

# def display():
#     try:
#         for i in range(4):
#             sleep(0.1)
#             print("hello: " +10)
#     except Exception as e:
#         print(e)

# def show():
#     try:
#         for i in range(4):
#             sleep(0.1)
#             print("hello")
#     except Exception as e:
#         print(e)

# threading.excepthook = custom_hook
# t1 = Thread(target = display)
# t2 = Thread(target = show)

# t1.start()
# t2.start()

# t1.join()
# t1.join()

# for i in range(4):
#     print("Bye")





# a pitfall in exception handling

# try:
#     f = open('data.txt', mode = 'r')
#     my_data = f.read()
#     print(my_data)
# except Exception as e:
#     print(e)
# else:
#     print("read operation success")
# finally:
#     f.close()


# try:
#     f = open('data.txt', mode = 'r')
#     my_data = f.read()
#     print(my_data)
# except Exception as e:
#     print(e)
# else:
#     print("read operation success")
# finally:
#     try:
#         f.close()
#     except Exception as e:
#         print(e)



try:
    f = open('data.txt', mode = 'r')
    my_data = f.read()
    print(my_data)
except Exception as e:
    print(e)
else:
    print("read operation success")
finally:
    try:
        f.close()
    except:
        pass