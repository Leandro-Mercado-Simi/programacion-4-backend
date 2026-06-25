from sqlmodel import SQLModel
from datetime import datetime


class ProductCategoryCreate(SQLModel):
    product_id: int
    category_id: int


class ProductCategoryRead(SQLModel):
    product_id: int
    category_id: int
    created_at: datetime
