import aiohttp
import asyncio
import time


async def get_pokemon(session, url):
    async with session.get(url) as resp:
        # Variant 1
        # try:
        #     pokemon = await resp.json()
        #     print(pokemon['name'])
        # except aiohttp.client_exceptions.ContentTypeError as content_type_error:
        #     print('Not correct ID of Pokemon')

        # Variant 2
        if resp.status == 200:
            pokemon = await resp.json()
            print(url.split('/')[-1], pokemon['name'])
        elif resp.status == 404:
            print('Not correct ID of Pokemon')
        else:
            print('Bad request')


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []

        for i in range(1, 201):
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{i}'
            tasks.append(asyncio.ensure_future(get_pokemon(session, pokemon_url)))

        original_pokemon = await asyncio.gather(*tasks)
        print()


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    print(f"Made in {(time.time() - start_time).__round__(2)} seconds")
    print(f"Process time is {time.process_time().__round__(2)} seconds")
