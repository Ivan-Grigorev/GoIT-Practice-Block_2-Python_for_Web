from threading import Thread
import time


class CountDownAndPrint(Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        for i in range(self.n):
            print(self.n - i, "left")
            time.sleep(1)


t = CountDownAndPrint(10)
t.start()
t.join()
print("How many have left?")
