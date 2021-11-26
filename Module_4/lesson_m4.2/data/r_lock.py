import threading

stack = 10
lock = threading.Lock()


def add_book():
    global stack
    lock.acquire()
    for i in range(100000):
        stack = stack + 1
    lock.release()


def take_book():
    global stack
    lock.acquire()
    for i in range(100000):
        stack = stack - 1
    lock.release()


t1 = threading.Thread(target=add_book, args=())
t2 = threading.Thread(target=take_book, args=())
t1.start()
t2.start()
t1.join()
t2.join()

print(stack)
