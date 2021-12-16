import aiohttp
import asyncio


async def index(session):
    url = 'https://python.org'
    async with session.get(url) as response:
        print(f'(index) Status: {response.status}')
        print(f'(index) Content-type: {response.headers["content-type"]}')

        html = await response.text()
        print(f'(index) Body: {len(html)}')


async def doc(session):
    url = 'https://python.org/doc/'
    async with session.get(url) as response:
        print(f'(doc) Status: {response.status}')
        print(f'(doc) Content-type: {response.headers["content-type"]}')

        html = await response.text()
        print(f'(doc) Body: {len(html)}')


async def main():
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(index(session), doc(session))


if __name__ == '__main__':
    asyncio.run(main())
