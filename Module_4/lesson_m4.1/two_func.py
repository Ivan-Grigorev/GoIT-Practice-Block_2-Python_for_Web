import os


def read_line(path):
    lst = []

    with open(path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            lst.append(int(line))

    return lst


def count_sum(ints):
    print('Started to count ')

    n = len(ints)
    counter = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if ints[i] + ints[j] + ints[k] == 0:
                    counter = +1
                    print(f"Result found {ints[i]}, {ints[j]}, {ints[k]}", end='\n')

    print(f"count ended: {counter}")
    return counter


if __name__ == "__main__":
    ints = read_line(os.path.abspath('data/data_list.txt'))

    count_sum(ints)

    print(input('Do you agree?[y/n]'))
    print('ended main')
