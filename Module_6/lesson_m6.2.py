import asyncio


async def tick():
    print("tick")
    await asyncio.sleep(1)
    print("tock")
    # return "Tick-Tock, Tick-Tock"


async def main():
    t1 = asyncio.create_task(tick(), name="tick1")
    t2 = asyncio.ensure_future(tick())

    # await t1
    # await t2

    # await asyncio.gather(t1,t2)

    result = await asyncio.gather(t1, t2)

    print(f'Task {t1.get_name()}, status = {t1.done()}')
    print(f'Task {t2.get_name()}, status = {t2.done()}')

    # for x in result:
    #     print(x)


if __name__ == '__main__':
    asyncio.run(main())


###################################
import asyncio
import time


async def tick():
    await asyncio.sleep(1)
    return "Tick"


async def tock():
    await asyncio.sleep(2)
    return "Tock"


async def main():
    start = time.perf_counter()

    t1 = asyncio.create_task(tick())
    t2 = asyncio.create_task(tock())

    # results = await asyncio.gather(t1,t2)
    # for i, result in enumerate(results, start=1):
    #     elapsed = time.perf_counter() - start
    #     print(f'Executed {i} in {elapsed:0.2f} seconds')
    #     print(result)

    for i, t in enumerate(asyncio.as_completed((t1, t2)), start=1):
        result = await t
        elapsed = time.perf_counter() - start
        print(f'Executed {i} in {elapsed:0.2f} seconds')
        print(result)


if __name__ == '__main__':
    asyncio.run(main())


################################
import asyncio


async def fetch_doc(doc):
    await asyncio.sleep(1)
    return doc


async def get_pages(docs):
    for cur_doc in docs:
        doc = await fetch_doc(cur_doc)
        for page in doc:
            await asyncio.sleep(1)
            yield page


async def main():
    async for page in get_pages(['doc1', 'doc2']):
        print(f'finally {page}')


if __name__ == '__main__':
    asyncio.run(main())


##################################
import asyncio


class AsyncIterator:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __aiter__(self):
        return self

    async def __anext__(self):
        print(f'Start {self.i}')
        await asyncio.sleep(1)
        print(f'End {self.i}')

        if self.i >= self.n:
            raise StopAsyncIteration
        self.i += 1
        return self.i


async def main():
    async for n in AsyncIterator(10):
        print(f'Finally {n}')


if __name__ == '__main__':
    asyncio.run(main())

# start 1
# start 2
# start 3


#####################################
from asyncio import FIRST_COMPLETED, ALL_COMPLETED
from collections import namedtuple
import aiohttp
import asyncio

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

services = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ipinfo', 'http://ipinfo.io/json', 'ip')
)


async def get_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def fetch_api(service):
    print(f'Fetching IP from {service.name}')

    json_response = await get_json(service.url)
    ip = json_response[service.ip_attr]
    await asyncio.sleep(2)
    return f'{service.name} finished with result: {ip}'


async def main():
    coros = [fetch_api(service) for service in services]
    done, pending = await asyncio.wait(coros, return_when=ALL_COMPLETED)

    for _ in pending:
        print(asyncio.current_task())

    for x in done:
        print(x.result(), x.done())


if __name__ == '__main__':
    asyncio.run(main())


####################################
import gevent


def foo():
    print('Running in foo')
    gevent.sleep(2)
    print('Explicit context switch to foo again')


def bar():
    print('Explicit context to bar')
    gevent.sleep(2)
    print('Implicit context switch back to bar')


gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
])


################################
import gevent
from gevent import Greenlet


def foo(message, n):
    """
    All thread in initialization will get
    a message and time for sleep
    """
    gevent.sleep(n)
    print(message)


def bar(x, y, n):
    gevent.sleep(n)
    print(x + y)


# Инициализация экземпляра Greenlet c передачей именнованой функции и её аргументов
# foo
thread1 = Greenlet.spawn(foo, "Hello", 1)

# Инициализация Greenlet с помощью обёртки от gevent
# функция foo с аргументами
thread2 = gevent.spawn(foo, "I live!", 2)

# Инициализация с помощью безымянной лямбда-функции
thread3 = gevent.spawn(bar, 1, 2, 2)

threads = [thread1, thread2, thread3]

# Блокировка до момента, когда задачи во всех потоках будут завершены
gevent.joinall(threads)


################################
import gevent
from gevent import Greenlet


class MyGreenlet(Greenlet):

    def __init__(self, message, n):
        Greenlet.__init__(self)
        self.message = message
        self.n = n

    def _run(self):
        print(self.message)
        gevent.sleep(self.n)


g = MyGreenlet("Hello go it", 1)
t = MyGreenlet("Same as threads", 1)
g.start()
g.join()
t.start()
t.join()


#################################
import gevent.monkey
from future.backports import urllib

gevent.monkey.patch_all()

import gevent
import requests


def fetch(pid):
    response = requests.get('http://jsontime.herokuapp.com/')
    result = response.json()
    datetime = result['datetime']

    print('Process %s: %s' % (pid, datetime))
    return result['datetime']


def synchronous():
    for i in range(1, 10):
        fetch(i)


def asynchronous():
    threads = []
    for i in range(1, 10):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)


print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()
