from typing import Callable
from fastapi import requests

async def middleware_1(request: requests.Request,  call_next: Callable):
    print("starting middleware 1")
    response = await call_next(request)
    print("ending middleware 1")
    return response
