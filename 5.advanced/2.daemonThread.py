# deamon thread : a thread that runs in the background, not important for program. 
# to run your program will not wait for daemon threads to complete before exiting. 
# non-daemon threads cannot normally be killed, they will stay alive until task is complete
# eg. background tasks, garbage collection, waiting for input, long running process

import threading
import time


# how long someone is logged in

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count +=1
        print("you have been logged in for " + str(count) +" seconds")


x = threading.Thread(target=timer,daemon=True)
# x.setDaemon(True) 
# x.isDaemon()

x.start()

answer = input("do you wanna exit? ")



# 5:58:20