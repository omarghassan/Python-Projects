
import time
from threading import Thread

def do_something():
    print("Starting ... ")
    time.sleep(2)
    print("Finished ... \n")
    time.sleep(1)

'''
#Sequentially
for i in range(5):
    do_something()
'''

'''
#In Parallel (I/O Bound)
for _ in range(5):
    the_thread = Thread(target = do_something, args = ())
    the_thread.start()
'''

#In Parallel (CPU Bound)

def cpu_bound():
    c = 0
    print("Starting ...")

    for i in range(20000000):
        c+= 1
    
    print("Finished ...")
    print("Value of c = ", c)

for _ in range(5):
    the_thread = Thread(target = cpu_bound, args = ())
    the_thread.start()

