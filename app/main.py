from fastapi import FastAPI, staticfiles, Request
from .routers import items, root
from .middleware import middleware_1, middleware_2

app = FastAPI()
app.add_middleware(middleware_2.Middleware2)
@app.middleware("http")
async def middleware(request: Request, call_next):
    return await middleware_1.middleware_1(request, call_next)

app.include_router(items.router, prefix="/items")
app.include_router(root.router, prefix="")
app.mount("/static", staticfiles.StaticFiles(directory="app/static"), name="static")
app.mount("/media", staticfiles.StaticFiles(directory="media"), name="media")
