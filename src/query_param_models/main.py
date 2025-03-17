from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from typing import Literal, Annotated

app = FastAPI()

class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []

@app.get("/hello")
async def hello():
    return {
        "message": "Hello World"
    }

@app.get("/items")
async def read_items(
    filter_query: Annotated[FilterParams, Query()],
):
    return filter_query
