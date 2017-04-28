import _thread
import time

def print_time(threadName, delay):
    for i in range(5):
        time.sleep(delay)
        print("%s:%s" % (threadName,time.ctime(time.time())))

try:
    _thread.start_new_thread(print_time,("Thread_1",2))
    _thread.start_new_thread(print_time,("Thread_2",4))
except:
    print("无法启动线程")



import threading

class MyThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

        