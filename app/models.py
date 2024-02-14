from typing import List

from fastapi import FastAPI, Query, Path
from pydantic import BaseModel

class Item(BaseModel):
    id: int | None
    name: str
    tags: List[str]
