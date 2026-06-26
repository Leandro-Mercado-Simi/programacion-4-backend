from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING
from decimal import Decimal
from sqlalchemy import Column, JSON, DateTime
from datetime import datetime, timezone

from app.modules.producto_categoria.model import ProductCategoryLink

if TYPE_CHECKING:
    from app.modules.categoria.model import Category


class Product(SQLModel, table=True):

    __tablename__ = "product"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(min_length=3, max_length=150, unique=True)
    description: Optional[str] = Field(default=None, max_length=255)
    base_price: Decimal = Field(gt=0)
    images_url: Optional[list[str]] = Field(default=None, sa_column=Column(JSON))
    stock: int
    min_stock: int
    available: bool = Field(default=True)

    categories: List["Category"] = Relationship(
        back_populates="products",
        link_model=ProductCategoryLink,
    )

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(DateTime(timezone=True), nullable=False),
    )

    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(DateTime(timezone=True), nullable=False),
    )

    deleted_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), nullable=True),
    )
