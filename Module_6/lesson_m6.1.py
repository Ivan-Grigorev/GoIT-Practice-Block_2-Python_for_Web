import time

from decorators import measure_time


def tick():
    print("Tick")
    time.sleep(1)
    print("Tock")


@measure_time
def main():
    for _ in range(3):
        tick()


if __name__ == "__main__":
    main()


#################################
import asyncio
from decorators import async_measure_time


async def tick():
    print("tick")
    await asyncio.sleep(1)
    print("tock")

    loop = asyncio.get_running_loop()
    if loop.is_running():
        print("Loop is still running")


async def main():
    awaitable_obj = asyncio.gather(tick(), tick(), tick())

    for task in asyncio.all_tasks():
        print(task, end='\n')

    await awaitable_obj


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
        print("Coroutines have finished")
    finally:
        loop.close()
        print("Loop closed")


##################################
import asyncio
from decorators import async_measure_time
from datetime import datetime


async def custom_sleep():
    print('SLEEP {}'.format(datetime.now()))
    await asyncio.sleep(1)


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print('Task {}: Compute factorial({})'.format(name, i))
        await custom_sleep()
        f *= i
    print('Task {}: factorial({}) is {}'.format(name, number, f))


@async_measure_time
async def main():
    await asyncio.gather(factorial("A", 3), factorial("B", 4), factorial("C", 5))


if __name__ == "__main__":
    asyncio.run(main())


####################################
import asyncio
from decorators import async_measure_time


async def addition(a, b):
    await asyncio.sleep(3)
    print("Addition Result       : ", a + b)


async def multiplication(a, b):
    await asyncio.sleep(1)
    print("Multiplication Result : ", a * b)


async def division(a, b):
    await asyncio.sleep(5)
    print("Division Result       : ", a / b)


async def subtraction(a, b):
    await asyncio.sleep(7)
    print("Subtraction Result    : ", a - b)


@async_measure_time
async def main():
    await asyncio.gather(division(10, 20),
                         subtraction(10, 20),
                         addition(10, 20),
                         multiplication(10, 20))


if __name__ == "__main__":
    asyncio.run(main())


###################################
import asyncio

import aiohttp
from decorators import async_measure_time


class Photo:
    def __init__(self, album_id, id, title, url, thumbnail_url):
        self.album_id = album_id
        self.id = id
        self.title = title
        self.url = url
        self.thumbnail_id = thumbnail_url

    @classmethod
    def from_json(cls, obj):
        return Photo(obj['albumId'], obj['id'], obj['title'], obj['url'], obj['thumbnailUrl'])


def print_photo_titles(photos):
    for photo in photos:
        print(f'{photo.title}', end='\n')


async def photos_by_album(task_name, album, session):
    print(f'{task_name}')
    url = f'https://jsonplaceholder.typicode.com/photos?albumId={album}'

    response = await session.get(url)
    photos_json = await response.json()

    return [Photo.from_json(photo) for photo in photos_json]


@async_measure_time
# async def main():
#     async with aiohttp.ClientSession() as session:
#         photos = await photos_by_album("Task1", 3, session)
#         print_photo_titles(photos)
async def main():
    async with aiohttp.ClientSession() as session:
        photos_in_albums = await asyncio.gather(*(photos_by_album(f'task{i + 1}', album, session)
                                                  for i, album in enumerate(range(2, 30))))

        photos_count = sum([len(cur) for cur in photos_in_albums])
        print(f'{photos_count=}')


#         print_photo_titles(photos)

if __name__ == "__main__":
    # asyncio.run(main())

    loop = asyncio.get_event_loop()
    try:
        loop.create_task(main())
        loop.run_forever()
    finally:
        loop.close()

####################################
import time
from functools import wraps


def measure_time(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        finish = time.perf_counter() - start
        print(f'Executed {func} in {finish:0.2f} seconds')
        return result

    return wrap


def async_measure_time(func):
    @wraps(func)
    async def wrap(*args, **kwargs):
        start = time.perf_counter()
        result = await func(*args, **kwargs)
        finish = time.perf_counter() - start
        print(f'Executed {func} in {finish:0.2f} seconds')
        return result

    return wrap


####################################
import asyncio
from decorators import async_measure_time


async def tick():
    print("Tick")
    await asyncio.sleep(1)
    print("Tock")

    loop = asyncio.get_running_loop()
    if loop.is_running():
        print("Loop is still running")


async def main():
    awaitable_obj = asyncio.gather(tick(), tick(), tick())

    for task in asyncio.all_tasks():
        print(task, end='\n')

    await awaitable_obj


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
        print("Coroutines have finished")
    finally:
        loop.close()
        print("Loop closed")
