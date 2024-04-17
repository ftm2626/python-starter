# thread = a flow of execution. li ke a seprate order of instructions.
# how each thread takes a turn running to aachieve concurrency
# GIL = (global interpreter lock)
# allows only one thread to hold the control of the python interpreter at any one 

# cpu bound = program/task spends most of it's time waiting for internal events(cpu intensive) -> use multiprocessing

# io bound = program/task spends amost of it's time waiting for external events(user input,  web scraping ) -> use multithreading

import threading

thread_count = threading.active_count()
thread_name = threading.enumerate()

print(thread_name)