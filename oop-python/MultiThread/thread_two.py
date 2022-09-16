from threading import Thread

def square_numbers():
    for i in range(100):
        i * i


if __name__ == "__main__":
    threads = []
    num_threads = 10

    # Create processes
    for i in range(num_threads):
        t = Thread(target=square_numbers)
        threads.append(t)

    # Start
    for t in threads:
        t.start()

    # Join
    for t in threads:
        t.join()

    print('end main')