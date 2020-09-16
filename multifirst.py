from threading import *
import time
def display():
    for i in range(1,10):
        time.sleep(5)
        print("Child thread excuting")
    print(current_thread().getName())

t=Thread(target=display)#creation of thread
t.start()

for i in range(1,10):
    time.sleep(1)
    print("main thread is executing")

print(current_thread().getName())
