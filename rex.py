from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
import random
app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


articles = ['pc', 'android', 'iphone', 'apple']
prices = [23.0, 45.3, 56.0, 100000.00]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    item = Item(name=random.choice(articles),
                price=random.uniform(prices[0], prices[3]).__round__(2),
                is_offer=False)

    return {"item_id": item_id,
            "detalle": q if q else 'Sin detalle',
            "item": item
            }


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
