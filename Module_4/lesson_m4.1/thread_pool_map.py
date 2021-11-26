import concurrent.futures
import time


def div(divisor, limit):
    print(f'starter div={divisor}')
    counter = 0
    for x in range(1, limit):
        if x % divisor == 0:
            counter += 1
            time.sleep(0.25)
    return counter


if __name__ == "__main__":
    print("started main")
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        result = executor.map(div, (3, 5, 3, 5), (25, 25, 35, 45))
        for r in result:
            print(r)
