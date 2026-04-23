from sqlmodel import SQLModel
from pydantic import Field
from typing import Optional


class ProductCreate(SQLModel):
    name: str = Field(..., max_length=100, example="Silla de Oficina")
    category_id: int
    price: float = Field(..., gt=0, example=150.50)
    stock: int = Field(..., ge=0, example=20)
    min_stock: int = Field(..., ge=0, example=5)


class ProductUpdate(SQLModel):
    # Opcional: Se usa si en el futuro se implementa PATCH (actualización parcial)
    name: Optional[str] = None
    category_id: Optional[int] = None
    price: Optional[float] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)
    min_stock: Optional[int] = Field(None, ge=0)
    is_active: Optional[bool] = None


class ProductRead(SQLModel):
    id: int
    name: str
    category_id: int
    price: float
    stock: int
    min_stock: int
    is_active: bool


class ProductStockResponse(SQLModel):
    stock: int
    below_min_stock: bool
    is_active: bool
