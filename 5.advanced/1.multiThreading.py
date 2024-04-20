# thread = a flow of execution. li ke a seprate order of instructions.
# how each thread takes a turn running to aachieve concurrency
# GIL = (global interpreter lock)
# allows only one thread to hold the control of the python interpreter at any one 

# cpu bound = program/task spends most of it's time waiting for internal events(cpu intensive) -> use multiprocessing

# io bound = program/task spends amost of it's time waiting for external events(user input,  web scraping ) -> use multithreading

import threading
import time

thread_count = threading.active_count()
thread_name = threading.enumerate()

print(thread_name)

# eg. finish three diffrent tasks in the morning

def eat_breakfast():
    time.sleep(3)
    print('you ate breakfast')
    return

def drink_coffee():
    time.sleep(4)
    print('you drank coffee')
    return

def study():
    time.sleep(5)
    print('you studied')
    return



# tasks done secuentially
# eat_breakfast()
# drink_coffee()
# study()

# tasks done concurrentlly(at the same time)
x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

duration_of_main_thread = time.perf_counter()
print(duration_of_main_thread)



# thread sync, a thread (main thread) wait for another thread to finish 

x.join() # main thread waits for thread x 
y.join()
z.join()