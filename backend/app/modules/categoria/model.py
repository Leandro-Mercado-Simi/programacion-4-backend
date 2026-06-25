from sqlmodel import Relationship, SQLModel, Field
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
