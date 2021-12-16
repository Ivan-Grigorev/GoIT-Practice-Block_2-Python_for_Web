import aiohttp
import asyncio
from uuid import uuid4


async def main():
    async with aiohttp.ClientSession(headers={'Request-Id': str(uuid4())}) as session:
        async with session.get('https://python.org') as response:
            print(f'Status: {response.status}')
            print(f'Content-type: {response.headers["content-type"]}')

            html = await response.text()
            print(f'Body: {len(html)}')


if __name__ == '__main__':
    asyncio.run(main())
