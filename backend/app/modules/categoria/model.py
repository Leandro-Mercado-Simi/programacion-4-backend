from sqlmodel import Relationship, SQLModel, Field
from sqlalchemy import Column, DateTime
from datetime import datetime, timezone
from typing import Optional, List, TYPE_CHECKING

from app.modules.producto_categoria.model import ProductCategoryLink

if TYPE_CHECKING:
    from app.modules.producto.model import Product


class Category(SQLModel, table=True):

    __tablename__ = "category"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=150)
    description: str = Field(max_length=255)
    is_active: bool = Field(default=True)

    products: List["Product"] = Relationship(
        back_populates="categories",
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
