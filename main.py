from fastapi import FastAPI
import uvicorn
from mylib.logic import wiki as wikilogic
from mylib.logic import search_wiki
from mylib.logic import phrase as wikiphrases


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wikipedia API. Call /search or /wiki"}


@app.get("/search/{value}")
async def search(value: str):
    "Search Wikipedia for names"
    result = search_wiki(value)
    return {"result": result}


@app.get("/wiki/{name}")
async def wiki(name: str):
    "Wikipedia fetcher"
    result = wikilogic(name)
    return {"result": result}


@app.get("/phrase/{name}")
async def phrase(name: str):
    "Wikipedia names and returns phrases"
    result = wikiphrases(name)
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
