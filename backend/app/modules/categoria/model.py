from sqlmodel import SQLModel, Field
from typing import Optional


class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    code: str = Field(max_length=6)
    description: str = Field(max_length=150)
    is_active: bool = Field(default=True)
