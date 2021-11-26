import os
import threading

from two_func import count_sum, read_line

if __name__ == "__main__":
    ints = read_line(os.path.abspath('data/data_list.txt'))

    t1 = threading.Thread(target=count_sum, args=(ints,))
    t1.start()

    print(input('Do you agree?[y/n]'))
    print('ended main')

"""1) daemon = true, t1 = join()"""
