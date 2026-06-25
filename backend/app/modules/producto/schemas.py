from typing import List, Optional
from decimal import Decimal
from sqlmodel import SQLModel


class ProductBase(SQLModel):
    name: str
    description: Optional[str] = None
    base_price: Decimal
    images_url: Optional[List[str]] = None
    stock: int
    min_stock: int
    available: bool = True


class ProductCreate(ProductBase):
    pass


class ProductUpdate(SQLModel):
    name: Optional[str] = None
    description: Optional[str] = None
    base_price: Optional[Decimal] = None
    images_url: Optional[List[str]] = None
    stock: Optional[int] = None
    min_stock: Optional[int] = None
    available: Optional[bool] = None


class ProductRead(ProductBase):
    id: int


class CategoryBasicRead(SQLModel):
    id: int
    name: str
    description: str


class ProductReadFull(ProductRead):
    categories: List[CategoryBasicRead] = []


class ProductStockResponse(SQLModel):
    stock: int
    below_min_stock: bool
    available: bool
