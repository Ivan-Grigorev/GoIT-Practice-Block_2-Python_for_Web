import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://python.org') as response:
            print(f'Status: {response.status}')
            print(f'Content-type: {response.headers}')

            html = await response.text()
            print(f'Body: {html[:100]}')


if __name__ == '__main__':
    asyncio.run(main())


# read() - bytes