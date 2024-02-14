from typing import Annotated, List, Dict

from fastapi import Query, APIRouter, exceptions, Body

from app.models import Item

router = APIRouter()
ITEMS: List[Item] = []

@router.get("/")
async def index() -> Dict[str, str]:
    return {"text": "items"}


@router.get("/read")
async def read_items(
    q: Annotated[str | None, Query()] = None,
    limit: Annotated[int | None, Query()] = None,
    offset: Annotated[int | None, Query()] = None,
):
    items = [i for i in ITEMS if q in i.name] if q else ITEMS
    start = offset or 0
    end = (start + limit) if limit else len(ITEMS)
    return items[start:end]


@router.get("/detail/{item_id}")
async def detail_item(item_id: int):
    for i in ITEMS:
        if i.id == item_id:
            return i
    raise exceptions.HTTPException(404, detail="Item not found!")


@router.put("/update/{item_id}")
async def update_item(item_id: int, data: Annotated[Item, Body()]):
    for index, i in enumerate(ITEMS):
        if i.id == item_id:
            item = {**data.model_dump(), **{"id": i.id}}
            ITEMS[index] = Item(**item)
            return item
    raise exceptions.HTTPException(404, detail="Item not found!")


@router.put("/create")
async def create_item(data: Item):
    data.id = len(ITEMS)
    ITEMS.append(data)
    return data
