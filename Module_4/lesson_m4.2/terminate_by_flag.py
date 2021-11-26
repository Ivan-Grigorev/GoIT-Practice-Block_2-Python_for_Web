import threading
import os
import time

from two_func import read_line, count_sum


class ThreeSumTask:
    def __init__(self, ints):
        self.ints = ints
        self.canceled = False

    def count_sum(self, ints):
        print('Started to count ')

        n = len(self.ints)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if self.canceled:
                        print("Task was canceled")
                        return

                    elif ints[i] + ints[j] + ints[k] == 0:
                        print(f"Result found {ints[i]}, {ints[j]}, {ints[k]}", end='\n')

    def run(self):
        self.count_sum(self.ints)

    def cancel(self):
        self.canceled = True


if __name__ == "__main__":
    ints = read_line(os.path.abspath('data/data_list.txt'))

    task = ThreeSumTask(ints)

    t = threading.Thread(target=task.run)

    t.start()

    time.sleep(5)

    task.cancel()

    #t1.join()
    print('Ended main')
