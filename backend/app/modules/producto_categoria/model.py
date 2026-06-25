from sqlmodel import SQLModel, Field
from datetime import datetime, timezone
from sqlalchemy import Column, DateTime


class ProductCategoryLink(SQLModel, table=True):

    __tablename__ = "product_category_link"

    product_id: int = Field(primary_key=True, foreign_key="product.id")
    category_id: int = Field(primary_key=True, foreign_key="category.id")

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(DateTime(timezone=True)),
    )
