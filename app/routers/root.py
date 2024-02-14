from typing import Dict
from fastapi import APIRouter, templating, responses, requests

from app import settings

router = APIRouter()
templates = templating.Jinja2Templates(directory="app/templates")


@router.get("/")
async def index() -> Dict[str, str]:
    return {"text": settings.env["APP_NAME"]}


@router.get("/html", response_class=responses.HTMLResponse)
async def read_item(request: requests.Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"text": settings.env["APP_NAME"]}
    )


@router.get("/redirect")
async def redirect_view():
    return responses.RedirectResponse("/")
