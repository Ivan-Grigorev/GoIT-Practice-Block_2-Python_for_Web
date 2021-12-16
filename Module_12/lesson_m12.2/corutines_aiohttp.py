import aiohttp
import asyncio
import time


async def get_pokemon(session, url):
    async with session.get(url) as resp:
        pokemon = await resp.json()
        print(pokemon['name'])


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []

        for i in range(1, 201):
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{i}'
            tasks.append(asyncio.ensure_future(get_pokemon(session, pokemon_url)))

        original_pokemon = await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    print(f"Made in {(time.time() - start_time).__round__(2)} seconds")
    print(f"Process time is {time.process_time().__round__(2)} seconds")
    # Made in 0.85 seconds
    # Made in 0.75 seconds
    # Made in 0.75 seconds

    # Average time is 0.78 seconds

    # Process time is 1.0 seconds
