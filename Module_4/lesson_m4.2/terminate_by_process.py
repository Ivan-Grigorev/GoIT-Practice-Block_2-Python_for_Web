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

    print('ended main')
