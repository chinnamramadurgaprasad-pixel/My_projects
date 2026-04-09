from fastapi import FastAPI
from .tools import search_tool

app = FastAPI()

@app.get("/search")
def search(query: str):
    return {"result": search_tool(query)}