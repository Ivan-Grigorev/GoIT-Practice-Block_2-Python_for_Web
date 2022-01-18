# pip install fastapi[all]

# OR

# pip install fastapi
# pip install uvicorn

from fastapi import FastAPI
from models import Greeting, Item, ItemValue

app = FastAPI()

db = {}


@app.get('/', response_model=Greeting)
async def hello():
    # return {'message': "Hello World!"}
    return Greeting(message="Hello World!")


@app.get('/items/{item}', response_model=Item)
async def items(item: int):
    try:
        # return {'item': db[item]}
        return Item(item=db[item])
    except KeyError:
        return Item()


@app.post('/add_item/{item}', response_model=ItemValue)
async def add_item(item: int, value: str):
    if item in db:
        return ItemValue(item=item, value=db[item], status='FAIL')
    else:
        db[item] = value
        # return {'item': item, 'value': db[item]}
        return ItemValue(item=item, value=db[item])


@app.post('/update_item/{item}', response_model=ItemValue)
async def update_item(item: int, value: str):
    if item in db:
        db[item] = value
        return ItemValue(item=item, value=db[item])
    else:
        return ItemValue(status='FAIL')
