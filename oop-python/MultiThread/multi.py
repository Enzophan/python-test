from multiprocessing import Process
import os
import time


def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

if __name__ == "__main__":
    processes = []
    num_processes = os.cpu_count()
    print('num_processes', num_processes)

    # Create processes
    for i in range(num_processes):
        p = Process(target=(square_numbers()))
        processes.append(p)

    # Start
    for p in processes:
        p.start()

    # Join
    for p in processes:
        p.join()

    print('end main')