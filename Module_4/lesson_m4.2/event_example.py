import os
import threading
from two_func import read_line, count_sum

if __name__ == "__main__":
    ints = read_line(os.path.abspath('data/data_list.txt'))
    event = threading.Event()


    def my_func():
        print("Waiting for event for trigger")
        event.wait()
        count_sum(ints)


    t1 = threading.Thread(target=my_func)
    t1.start()

    x = input("do you want to start this event?[y/n]")
    if x == 'y':
        event.set()
    print(f'\n{event.is_set()}')
