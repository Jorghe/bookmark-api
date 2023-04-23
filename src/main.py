from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from deta import Deta


app = FastAPI()

deta = Deta()

db = deta.Base("bookmarks")

directory = Jinja2Templates(directory="templates")

@app.get("/")
def render_index():

    return {"Bookmark API": "Is on Space!"}

@app.get("/home", response_class=HTMLResponse)
def go_home(request: Request):
    return directory.TemplateResponse("home.html",
    {
        "request": _req,

    })