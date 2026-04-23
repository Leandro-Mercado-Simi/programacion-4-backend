from sqlmodel import SQLModel
from pydantic import Field
from typing import Optional


class CategoryCreate(SQLModel):
    code: str = Field(..., pattern=r"^[A-Z]{3}-\d{2}$", example="MUE-01")
    description: str = Field(..., min_length=3, example="Muebles de Oficina")
    is_active: bool = True


class CategoryUpdate(SQLModel):
    code: Optional[str] = Field(None, pattern=r"^[A-Z]{3}-\d{2}$")
    description: Optional[str] = Field(None, min_length=3)
    is_active: Optional[bool] = None


class CategoryRead(SQLModel):
    id: int
    code: str
    description: str
    is_active: bool
