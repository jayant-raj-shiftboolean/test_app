from fastapi import FastAPI, Query
from pydantic import HttpUrl, BaseModel

app = FastAPI()

# @app.get("/users")
# async def read_users():
#     return ["Rick", "Morty"]


# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}


@app.get("/users/")
async def read_user(user_id: str | None = Query("sdk", max_length=5)):
    if user_id:
        return {"user_id": user_id}
    return {"user": None}


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    images: list[Image] | None = None


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item


@app.get("/items/", response_model=list[Item])
async def read_items():
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]
