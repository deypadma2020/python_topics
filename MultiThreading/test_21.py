# Need of Condition object: -
    # 1. To communicate with multiple threads.
    # 2. Event object: - communication between two threads

# Methods: -
    # 1. acquire()
    # 2. release()
    # 3. wait(timeout=0)
    # 4. notify()
    # 5. notify_all()

# THESE METHODS MUST ONLY BE CALLED WHEN THE CALLING THREAD HAS ACQUIRED THE LOCK

import threading 
import time

con = threading.Condition()

def write_data():
    con.acquire()

    with open('output/report.txt', 'w') as file1:
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        for day in days:
            temp = input(f"Enter the temparature for {day}: ")
            file1.write(temp+"\n")

    con.notify_all()
    con.release()

def max_temp():
    con.acquire()
    con.wait(timeout=0)

    with open('output/report.txt', 'r') as file1:
        data=file1.readlines()
        max1=float(data[0].strip("\n"))

        for temp in data[1:]:
            temp=float(temp.strip("\n"))
            if temp > max1:
                max1 = temp

        print("Maximum temparature is: ", max1)

        con.release()

def avg_temp():
    con.acquire()
    con.wait(timeout=0)

    with open("output/report.txt", mode='r') as file1:
        data = file1.readlines()
        sum1 = 0

        for temp in data:
            temp = float(temp.strip("\n"))
            sum1 = sum1 + temp

        avg = sum1/len(data)
        print("Average temparature for week: ", avg)
    con.release()

t1 = threading.Thread(target=write_data)
t2 = threading.Thread(target=max_temp)
t3 = threading.Thread(target=avg_temp)

t1.run()
t2.run()
t3.run()