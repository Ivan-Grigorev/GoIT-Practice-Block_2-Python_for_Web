import threading
import time
import random
import datetime


class Race:
    def __init__(self):
        self.barrier = threading.Barrier(4)
        self.cars = ['Porsche', 'Mercedes-Benz', 'Audi', 'BMW']

    def lead(self):
        car = self.cars.pop()
        time.sleep(random.randrange(1, 5))
        print(f'\n{car} reached the barrier at {datetime.datetime.now()}')
        self.barrier.wait()

        time.sleep(random.randrange(1, 5))
        print(f'\n{car} started race at {datetime.datetime.now()}')

        time.sleep(random.randrange(1, 5))
        print(f'\n{car} finished race at {datetime.datetime.now()}')

        self.barrier.wait()
        print(f'\nDriver of {car} go to have a rest')


if __name__ == "__main__":
    print('Race preparation')

    race = Race()
    for x in range(4):
        t = threading.Thread(target=race.lead)
        t.start()
