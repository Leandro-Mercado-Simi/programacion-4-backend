from typing import List, Optional
from decimal import Decimal
from datetime import datetime
from sqlmodel import SQLModel


class CategoryBase(SQLModel):
    name: str
    description: str
    is_active: bool = True


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(SQLModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None


class CategoryRead(CategoryBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None


class ProductBasicRead(SQLModel):
    id: int
    name: str
    base_price: Decimal
    available: bool


class CategoryReadFull(CategoryRead):
    products: List[ProductBasicRead] = []


class CategoryPaginatedResponse(SQLModel):
    total: int
    items: List[CategoryReadFull]
