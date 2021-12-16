import asyncio
import aiohttp


async def main():
    async with aiohttp.ClientSession() as session:
        pokemon_url = 'https://pokeapi.co/api/v2/pokemon/1'

        async with session.get(pokemon_url) as resp:
            pokemon = await resp.json()
            print(pokemon['name'])


if __name__ == '__main__':
    asyncio.run(main())
