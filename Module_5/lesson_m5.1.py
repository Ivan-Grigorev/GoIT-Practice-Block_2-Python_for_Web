import multiprocessing
import time
import sys


def daemon():
    p = multiprocessing.current_process()
    print('Starting: ', p.name, p.pid)
    sys.stdout.flush()
    time.sleep(2)
    print('Exiting: ', p.name, p.pid)
    sys.stdout.flush()


def non_daemon():
    p = multiprocessing.current_process()
    print('Starting: ', p.name, p.pid)
    sys.stdout.flush()
    print('Exiting: ', p.name, p.pid)
    sys.stdout.flush()


if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon', target=daemon)
    d.daemon = True

    n = multiprocessing.Process(name='non-daemon', target=non_daemon)
    n.daemon = False

    d.start()
    time.sleep(1)
    n.start()


##################################
import multiprocessing
import time
import sys


def daemon():
    p = multiprocessing.current_process()
    print('Starting:', p.name, p.pid)
    sys.stdout.flush()
    time.sleep(2)
    print('Exiting :', p.name, p.pid)
    sys.stdout.flush()


def non_daemon():
    p = multiprocessing.current_process()
    print('Starting:', p.name, p.pid)
    sys.stdout.flush()
    print('Exiting :', p.name, p.pid)
    sys.stdout.flush()


if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon', target=daemon)
    d.daemon = True

    n = multiprocessing.Process(name='non-daemon', target=non_daemon)
    n.daemon = False

    d.start()
    time.sleep(1)
    n.start()


################################
import multiprocessing
import time

start = time.perf_counter()


def func():
    print("Start doing")
    time.sleep(1)
    print("Stop doing")


# func()
func()

# p1 = multiprocessing.Process(target=func)
# p2 = multiprocessing.Process(target=func)
# p1.start()
# p2.start()
# p1.join()
# p2.join()

# processes = []
#
# for _ in range(8):
#     p = multiprocessing.Process(target=func)
#     p.start()
#     processes.append(p)
#
# for process in processes:
#     process.join()


finish = time.perf_counter()

print(f'Finished at {round(finish - start, 2)} sec.')


###################################
import time
from multiprocessing import Process, RLock


def printer(item, lock):

    lock.acquire()
    try:
        print(item)
        time.sleep(2)
    finally:
        lock.release()


if __name__ == '__main__':
    lock = RLock()
    items = ['article', 'thesis', 'report']

    for item in items:
        p = Process(target=printer, args=(item, lock))
        p.start()


##################################
import time
from multiprocessing import Pool


def sum_square(number):
    s = 0
    for i in range(number):
        s += i * i
    return s


if __name__ == "__main__":
    numbers = range(25000)

    start = time.perf_counter()

    with Pool(processes=8) as p:
        p.map(sum_square, numbers)

    finish = time.perf_counter()

    print(f'Finished at {round(finish - start, 2)} sec.')


#################################
from multiprocessing import Pool
import functools


def inc(x):
    return x + 1


def dec(x):
    return x - 1


def add(x, y):
    return x + y


def smap(f):
    return f()


f_inc = functools.partial(inc, 4)
f_dec = functools.partial(dec, 2)
f_add = functools.partial(add, 3, 4)

if __name__ == '__main__':
    with Pool() as pool:
        res = pool.map(smap, [f_inc, f_dec, f_add])

        print(res)


#################################
from multiprocessing import Pool
import functools


def inc(x):
    return x + 1


def dec(x):
    return x - 1


def add(x, y):
    return x + y


def smap(f):
    return f()


f_inc = functools.partial(inc, 4)
f_dec = functools.partial(dec, 2)
f_add = functools.partial(add, 3, 4)

if __name__ == '__main__':
    with Pool() as pool:
        res = pool.map(smap, [f_inc, f_dec, f_add])

        print(res)


##############################
import time

from two_func import read_line, count_sum
import multiprocessing
import os

if __name__ == "__main__":
    ints = read_line(os.path.abspath('data/data_list.txt'))

    start = time.perf_counter()

    with multiprocessing.Pool(processes=4) as p:
        p.map(count_sum, (ints,))

    finish = time.perf_counter()

    print(f'Finished at {round(finish - start, 2)} sec.')


################################
from concurrent.futures import ProcessPoolExecutor
import os


def task():
    print("Executing our Task on Process: {}".format(os.getpid()))


if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=2) as executor:
        task1 = executor.submit(task)
        task2 = executor.submit(task)


################################
# from multiprocessing import Process
# import time
#
#
# class CountDownAndPrint(Process):
#     def __init__(self, n):
#         super().__init__()
#         self.n = n
#
#     def run(self):
#         for i in range(self.n):
#             print(self.n - i, "left")
#             time.sleep(1)
#
#
# if __name__ == '__main__':
#     p = CountDownAndPrint(10)
#     p.start()
#     p.join()
#     print("How many have left?")
#
#
import time
from multiprocessing import Process


class Worker(Process):

    def run(self):
        print(f'In {self.name}')
        time.sleep(2)


if __name__ == '__main__':
    worker = Worker()
    worker.start()

    worker2 = Worker()
    worker2.start()

    worker.join()
    worker2.join()


#################################
import os
import multiprocessing
import time

from two_func import count_sum, read_line

if __name__ == "__main__":
    ints = read_line(os.path.abspath('data/data_list.txt'))

    p = multiprocessing.Process(target=count_sum, args=(ints,))
    p.start()

    time.sleep(5)

    p.terminate()

    print('Ended main')


##############################
import os
import time


def read_line(path):
    lst = []

    with open(path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            lst.append(int(line))

    return lst


def count_sum(ints):
    start = time.perf_counter()
    print('Started to count')

    n = len(ints)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if ints[i] + ints[j] + ints[k] == 0:
                    print(f"Result found {ints[i]}, {ints[j]}, {ints[k]}", end='\n')


if __name__ == "__main__":
    ints = read_line(os.path.abspath('data/data_list.txt'))

    count_sum(ints)

    print(input('Do you agree?[y/n]'))
    print('Ended main')
