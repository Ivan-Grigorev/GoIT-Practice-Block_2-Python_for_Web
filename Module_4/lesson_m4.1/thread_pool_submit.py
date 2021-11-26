import concurrent.futures
import time


def div(divisor, limit):
    print(f'starter div={divisor}')

    for x in range(1, limit):
        if x % divisor == 0:
            print(f'divisor={divisor}, x ={x}')
        time.sleep(0.25)
    print(f'ended div={divisor}', end='\n')


if __name__ == "__main__":
    print("started main")

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(div, 3, 25)
        executor.submit(div, 5, 25)
        print("Printed after submit")

    print("Process finished")

    # executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
    # executor.submit(div, 3, 25)
    # executor.submit(div, 5, 25)
    #
    # executor.shutdown(wait=False)
    #
    # print('\n main ended')
