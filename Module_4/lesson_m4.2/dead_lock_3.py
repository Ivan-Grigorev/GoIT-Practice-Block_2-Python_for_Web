import threading
import time

a = 5
b = 5

a_lock = threading.Lock()
b_lock = threading.Lock()


def calc():
    global a
    global b
    print('T1 acquiring lock a')
    a_lock.acquire()
    time.sleep(5)
    print('T2 acquiring lock b')
    b_lock.acquire()
    time.sleep(5)

    a += 5
    b += 5

    print('Releasing both locks')
    a_lock.release()
    b_lock.release()


def calc2():
    global a
    global b
    print('T2 acquiring lock b')
    b_lock.acquire()
    time.sleep(5)
    print('T2 acquiring lock a')
    a_lock.acquire()
    time.sleep(5)

    a += 10
    b += 10

    print('Releasing both locks')
    b_lock.release()
    a_lock.release()


if __name__ == "__main__":
    t1 = threading.Thread(target=calc)
    t1.start()
    t2 = threading.Thread(target=calc2)
    t2.start()
