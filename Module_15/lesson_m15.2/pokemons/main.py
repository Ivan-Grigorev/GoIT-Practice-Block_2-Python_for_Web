from fastapi import FastAPI
from models import Pokemon
import aiohttp

app = FastAPI()


@app.get('/pokemon/{pokemon_id}', response_model=Pokemon)
async def get_pokemon_by_id(pokemon_id: int):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}') as resp:
            pokemon = await resp.json()
            return Pokemon(id=pokemon['id'],
                           name=pokemon['name'],
                           base_experience=pokemon['base_experience'],
                           height=pokemon['height'],
                           is_default=pokemon['is_default'],
                           order=pokemon['order'],
                           weight=pokemon['weight'],
                           abilities=pokemon['abilities'],
                           forms=pokemon['forms'])
