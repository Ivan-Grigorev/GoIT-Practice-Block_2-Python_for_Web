from pydantic import BaseModel


class Greeting(BaseModel):
    message: str


class Item(BaseModel):
    item: str = None


class ItemValue(BaseModel):
    item: str = None
    value: str = None
    status: str = 'OK'
