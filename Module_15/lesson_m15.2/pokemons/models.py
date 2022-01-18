from pydantic import BaseModel, HttpUrl
from typing import Optional, List


class NamedAPIResource(BaseModel):
    name: str
    url: HttpUrl


class PokemonAbility(BaseModel):
    is_hidden: bool
    slot: int
    ability: Optional[NamedAPIResource] = None


class Pokemon(BaseModel):
    id: int
    name: str
    base_experience: int
    height: int
    is_default: bool
    order: int
    weight: int
    abilities: List[PokemonAbility]
    forms: List[NamedAPIResource]

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
