from multiprocessing import Pool


def cube(number):
    return number * number * number

if __name__ == "__main__":

    numbers = range(10)
    pool = Pool()

    # Map, Apply, Join, Close
    retsult = pool.map(cube, numbers)
    # pool.apply(cube,numbers[0])

    pool.close()
    pool.join()

    print(retsult)


   
