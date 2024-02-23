from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from deta import Deta
from typing import Union, Any
from pydantic import BaseModel

app = FastAPI()

deta = Deta()

db = deta.Base("bookmarks")

app.mount("/static", StaticFiles(directory="static"), name="static")

directory = Jinja2Templates(directory="templates")

class Cumulo(BaseModel):
    name: str
    description: Union[str, None] = None
    url: str
    tags: list[str] = []

@app.get("/", response_class=HTMLResponse)
def go_home(request: Request):
    return directory.TemplateResponse("home.html",
    {
        "request": request,

    })


@app.get("/cumulo/", response_model=list[Cumulo])
async def read_items() -> Any:
    return [
        Cumulo(name="Portal Gun", description="", tags=[], url="42.0"),
        Cumulo(name="Plumbus", description="", tags=[], url="32.0"),
    ]