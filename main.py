from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int 
    name: str
    description: str

db = {}

@app.get("/items")
def get_items():
    return list(db.values())

@app.post("/items")
def create_item(item: Item):
    db[item.id] = item.dict()
    return item

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    db[item_id] = item.dict()
    return item

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    db.pop(item_id, None)
    return {"deleted": item_id}
