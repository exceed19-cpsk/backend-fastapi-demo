from fastapi import APIRouter, Body
from typing import Union, Optional
from pydantic import BaseModel

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)


class Item(BaseModel):
    item_id: Union[int, str]
    item_name: str
    item_bool: bool


class ItemDetail(BaseModel):
    item_color: str
    item_detail: str


@router.get("/1/foo/true")
def show_item1():
    return {"msg": "order"}

@router.get("/{item_id}/{item_name}/{item_bool}")
def show_item(item_id: Union[int, str], item_name: str, item_bool: bool):
    print(type(item_id), type(item_name), type(item_bool))
    return {"item_id": item_id, "item_name": item_name, "item_bool": item_bool}

@router.post("/", status_code=201)
def create_item():
    return {"msg": "created"}

@router.get("/")
def query_item(item_id: int = 0, item_name: str = " ", item_bool: Union[bool, None] = False):
    if item_bool:
        return {"item_id": item_id, "item_name": item_name}
    return {"item_id": item_id, "item_name": item_name, "item_bool": item_bool}

@router.get("/with_body")
def show_item_body(item: Item, detail: ItemDetail):
    new_item_id = "s" + str(item.item_id)

    return {"item": item, "detail": detail}

@router.get("/with_body_with_params")
def show_item_body_with_query(item: Item, item_color: str = Body()):
    return {"item": item, "item_color": item_color}

@router.get("/combine/{item_id}")
def combine_all_params(item_id: str, item_name: str, item_detail: ItemDetail):
    return {"item_id": item_id, "item_name": item_name, "item_detail": item_detail}