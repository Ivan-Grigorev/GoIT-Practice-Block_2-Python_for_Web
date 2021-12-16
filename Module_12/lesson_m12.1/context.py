import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        response = await session.get('https://python.org')

        print(f'Status: {response.status}')
        print(f'Content-type: {response.headers}')

        html = await response.text()
        response.close()
        print(f'Body: {html[:100]}')


if __name__ == '__main__':
    asyncio.run(main())
