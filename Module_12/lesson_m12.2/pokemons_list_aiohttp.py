import asyncio
import aiohttp
import time


async def main():
    async with aiohttp.ClientSession() as session:
        for i in range(1, 201):
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{i}'

            async with session.get(pokemon_url) as resp:
                pokemon = await resp.json()
                print(pokemon['name'])


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    print(f"Made in {(time.time() - start_time).__round__(2)} seconds")
    print(f"Process time is {time.process_time().__round__(2)} seconds")
    # Made in 3.69 seconds
    # Made in 3.19 seconds
    # Made in 2.99 seconds

    # Average time is 3.29 seconds

    # Process time is 1.02 seconds

