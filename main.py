from fastapi import FastAPI, Body
from typing import Union, Optional
from pydantic import BaseModel


class Item(BaseModel):
    item_id: Union[int, str]
    item_name: str
    item_bool: bool


class ItemDetail(BaseModel):
    item_color: str
    item_detail: str


"""
class Item(BaseModel):
    item_id: Union[int, str]
    item_name: str
    item_bool: bool
    item_details: ItemDetail

req example:
{
    item_id: xxx,
    item_name: xxx,
    item_bool: xxx,
    item_details: {
        item_color: xxx,
        item_detail: xxx
    }
}
"""


app = FastAPI()

@app.get("/")
def root():
    return {"msg": "welcome to root page"}

@app.get("/items/1/foo/true")
def show_item1():
    return {"msg": "order"}

@app.get("/items/{item_id}/{item_name}/{item_bool}")
def show_item(item_id: Union[int, str], item_name: str, item_bool: bool):
    print(type(item_id), type(item_name), type(item_bool))
    return {"item_id": item_id, "item_name": item_name, "item_bool": item_bool}

@app.post("/items", status_code=201)
def create_item():
    return {"msg": "created"}

@app.get("/items")
def query_item(item_id: int = 0, item_name: str = " ", item_bool: Union[bool, None] = False):
    if item_bool:
        return {"item_id": item_id, "item_name": item_name}
    return {"item_id": item_id, "item_name": item_name, "item_bool": item_bool}

@app.get("/items/with_body")
def show_item_body(item: Item, detail: ItemDetail):
    new_item_id = "s" + str(item.item_id)

    return {"item": item, "detail": detail}

@app.get("/items/with_body_with_params")
def show_item_body_with_query(item: Item, item_color: str = Body()):
    return {"item": item, "item_color": item_color}

@app.get("/items/combine/{item_id}")
def combine_all_params(item_id: str, item_name: str, item_detail: ItemDetail):
    return {"item_id": item_id, "item_name": item_name, "item_detail": item_detail}
