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
    print('Started to count ')

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

###################################
from multiprocessing import Process, Lock
from multiprocessing.sharedctypes import Value, Array
from ctypes import Structure, c_double


class Point(Structure):
    _fields_ = [('x', c_double), ('y', c_double)]


def modify(n, x, s, A):
    n.value **= 2
    x.value **= 2
    s.value = s.value.upper()
    for a in A:
        a.x **= 2
        a.y **= 2


lock = Lock()

n = Value('i', 7)
x = Value(c_double, 1.0 / 3.0, lock=False)
s = Array('c', b'hello world', lock=lock)
A = Array(Point, [(1, -6), (-5, 2), (2, 9)], lock=lock)

p = Process(target=modify, args=(n, x, s, A))
p.start()
p.join()

print(n.value)  # 49
print(x.value)  # 0.1111111111111111
print(s.value)  # b 'HELLO WORLD'
print([(a.x, a.y) for a in A])

###############################
import multiprocessing


def print_records(records):
    """
    function to print record(tuples) in records(list)
    """
    for record in records:
        print(f"Name: {record[0]}\nScore: {record[1]}\n")


def insert_record(record, records):
    """
    function to add a new record to records(list)
    """
    records.append(record)
    print("New record added!\n")


if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        # creating a list in server process memory
        records = manager.list([('Sam', 10), ('Adam', 9), ('Kevin', 9)])
        # new record to be inserted in records
        new_record = ('Jeff', 8)

        # creating new processes
        p1 = multiprocessing.Process(target=insert_record, args=(new_record, records))
        p2 = multiprocessing.Process(target=print_records, args=(records,))

        # running process p1 to insert new record
        p1.start()
        p1.join()

        # running process p2 to print records
        p2.start()
        p2.join()

#################################
import multiprocessing


def print_records(records):
    """
    function to print record(tuples) in records(list)
    """
    for record in records:
        print(f"Name: {record[0]}\nScore: {record[1]}\n")


def insert_record(record, records):
    """
    function to add a new record to records(list)
    """
    records.append(record)
    print("New record added!\n")


if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        # creating a list in server process memory
        records = manager.list([('Sam', 10), ('Adam', 9), ('Kevin', 9)])
        # new record to be inserted in records
        new_record = ('Jeff', 8)

        # creating new processes
        p1 = multiprocessing.Process(target=insert_record, args=(new_record, records))
        p2 = multiprocessing.Process(target=print_records, args=(records,))

        # running process p1 to insert new record
        p1.start()
        p1.join()

        # running process p2 to print records
        p2.start()
        p2.join()

###################################
from multiprocessing import Process, Queue

sentinel = -1


def creator(data, q):
    """
    Creates data to be consumed and waits for the consumer
    to finish processing
    """
    print('Creating data and putting it on the queue')
    for item in data:
        q.put(item)


def my_consumer(q):
    """
    Consumes some data and works on it
    In this case, all it does is double the input
    """
    while True:
        data = q.get()
        print('Data found to be processed: {}'.format(data))

        processed = data * 2
        print(processed)

        if data is sentinel:
            break


if __name__ == '__main__':
    q = Queue()
    data = [5, 10, 13, -1]

    process_one = Process(target=creator, args=(data, q))
    process_two = Process(target=my_consumer, args=(q,))

    process_one.start()
    process_two.start()

    process_one.join()
    process_two.join()

######################################
import multiprocessing


def square_list(my_list, q):
    """
    function to square a given list
    """
    # append squares of my_list to queue
    for num in my_list:
        q.put(num * num)


def print_queue(q):
    """
    function to print queue elements
    """
    print("Queue elements: ")
    while not q.empty():
        print(q.get())
    print("Queue is now empty!")


if __name__ == "__main__":
    # input list
    my_list = [1, 2, 3, 4]

    # creating multiprocessing Queue
    q = multiprocessing.Queue()

    # creating new processes
    p1 = multiprocessing.Process(target=square_list, args=(my_list, q))
    p2 = multiprocessing.Process(target=print_queue, args=(q,))

    # running process p1 to square list
    p1.start()
    p1.join()

    # running process p2 to get queue elements
    p2.start()
    p2.join()

#######################################
import multiprocessing


def square_list(my_list, result):
    """
    function to square a given list
    """
    # append squares of my_list to result array
    for idx, num in enumerate(my_list):
        result[idx] = num * num

    # print result Array
    print("Result (in process p1): {}".format(result[:]))


if __name__ == "__main__":
    # input list
    my_list = [1, 2, 3, 4]

    # creating Array of int data type with space for 4 integers
    result = multiprocessing.Array('i', 4)

    # creating new process
    p1 = multiprocessing.Process(target=square_list, args=(my_list, result))

    # starting process
    p1.start()

    # wait until process is finished
    p1.join()

    # print result array
    print("Result (in main program): {}".format(result[:]))

####################################
import multiprocessing


def square_list(my_list, result, square_sum):
    """
    function to square a given list
    """
    # append squares of my_list to result array
    for idx, num in enumerate(my_list):
        result[idx] = num * num

    # square_sum value
    square_sum.value = sum(result)

    # print result Array
    print("Result (in process p1): {}".format(result[:]))

    # print square_sum Value
    print("Sum of squares (in process p1): {}".format(square_sum.value))


if __name__ == "__main__":
    # input list
    my_list = [1, 2, 3, 4]

    # creating Array of int data type with space for 4 integers
    result = multiprocessing.Array('i', 4)

    # creating Value of int data type
    square_sum = multiprocessing.Value('i')

    # creating new process
    p1 = multiprocessing.Process(target=square_list, args=(my_list, result, square_sum))

    # starting process
    p1.start()

    # wait until process is finished
    p1.join()

    # print result array
    print("Result (in main program): {}".format(result[:]))

    # print square_sum Value
    print("Sum of squares (in main program): {}".format(square_sum.value))

#####################################
import sched
import time

# instance is created
scheduler = sched.scheduler(time.time, time.sleep)


# function to print time
# and name of the event
def print_event(name):
    print('EVENT: ', time.time(), name)


# printing starting time
print('START: ', time.time())

# first event with delay of
# 1 second
e1 = scheduler.enter(1, 1, print_event, ('1st',))

# second event with delay of
# 2 seconds
e2 = scheduler.enter(2, 1, print_event, ('2nd',))

# executing the events
scheduler.run()
