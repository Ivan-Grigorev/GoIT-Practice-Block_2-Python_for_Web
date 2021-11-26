import threading
import time


def consumer(cond):
    print('Starting consumer thread')
    t = threading.currentThread()
    with cond:
        cond.wait()
        print('Resource is available to consumer')


def producer(cond):
    """set up the resource to be used by the consumer"""
    print('Starting producer thread')
    with cond:
        print('Making resource available')
        cond.notify_all()


condition = threading.Condition()
c1 = threading.Thread(name='c1', target=consumer, args=(condition,))
c2 = threading.Thread(name='c2', target=consumer, args=(condition,))
p = threading.Thread(name='p', target=producer, args=(condition,))

c1.start()
time.sleep(2)
c2.start()
time.sleep(2)
p.start()
