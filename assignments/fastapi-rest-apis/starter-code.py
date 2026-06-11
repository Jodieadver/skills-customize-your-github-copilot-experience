from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

items = [
    Item(id=1, name="Notebook", description="A spiral notebook", price=4.99),
    Item(id=2, name="Pencil", description="A graphite pencil", price=0.99),
]

@app.get("/items")
def read_items():
    return items

@app.get("/items/{item_id}")
def read_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items", status_code=201)
def create_item(item: ItemCreate):
    new_id = max((existing.id for existing in items), default=0) + 1
    new_item = Item(id=new_id, **item.dict())
    items.append(new_item)
    return new_item

@app.put("/items/{item_id}")
def update_item(item_id: int, item_update: ItemCreate):
    for index, existing in enumerate(items):
        if existing.id == item_id:
            updated_item = Item(id=item_id, **item_update.dict())
            items[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, existing in enumerate(items):
        if existing.id == item_id:
            items.pop(index)
            return {"detail": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")

# Example commands for testing:
# curl -X GET "http://127.0.0.1:8000/items"
# curl -X POST "http://127.0.0.1:8000/items" -H "Content-Type: application/json" -d '{"name":"Eraser","price":1.50}'
# curl -X PUT "http://127.0.0.1:8000/items/1" -H "Content-Type: application/json" -d '{"name":"Notebook","price":5.99,"description":"Updated notebook","in_stock":true}'
# curl -X DELETE "http://127.0.0.1:8000/items/1"
