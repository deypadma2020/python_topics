from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "This ia very important"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = "padma"):
    return {"item_id": item_id, "q": q}






# fastapi dev main.py
# uvicorn main:app --reload