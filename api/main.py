from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def render_index():
    return {"Bookmark API": "Is not on Space!"}
