from sqlmodel import SQLModel, Field
from typing import Optional


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100)
    category_id: int = Field(foreign_key="category.id")
    price: float
    stock: int
    min_stock: int
    is_active: bool = Field(default=True)
