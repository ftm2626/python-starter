# multiprocessing : running tasks in parallel of diffrent cpu cores, bypasses GIL used for threads

# multiprocessing : better for cpu bound tasks(heavy cpu usage)
# multithreading : better for io bound tasks(waiting around)

from multiprocessing import Process, cpu_count
import time



def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    a = Process(target=counter,args=(100000,))
    b = Process(target=counter,args=(100000,))
    a.start()
    b.start()

    a.join()
    b.join()



    print("Finishded in : " , time.perf_counter())
    print(cpu_count())



if __name__ == "__main__":
    main() #for windows os