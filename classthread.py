from threading import *

class MyThread(Thread):
    def run(self):
        for i in range(1,10):
            print(i)

t=MyThread()
t.start()

for i in range(1,30):
    print(i)
print(current_thread().getName())