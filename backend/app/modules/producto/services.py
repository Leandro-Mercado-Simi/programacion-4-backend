from sqlmodel import Session, select, func
from typing import List, Tuple, Optional
from sqlalchemy.orm import selectinload
from datetime import datetime, timezone

from .model import Product
from .schemas import (
    ProductCreate,
    ProductUpdate,
    ProductRead,
    ProductReadFull,
    ProductStockResponse,
)


# Método para persistir un nuevo producto
def service_create_product(session: Session, data: ProductCreate) -> ProductRead:
    product = Product.model_validate(data)
    session.add(product)
    session.commit()
    session.refresh(product)
    return ProductRead.model_validate(product)


# Método para listar todos los productos disponibles
def service_get_all_products(
    session: Session,
    offset: int = 0,
    limit: int = 20,
    name: Optional[str] = None,
    available: Optional[bool] = None,
) -> Tuple[int, List[Product]]:
    query = select(Product).options(selectinload(Product.categories))

    if name:
        query = query.where(Product.name.ilike(f"%{name}%"))
    if available is not None:
        query = query.where(Product.available == available)

    count_query = select(func.count()).select_from(query.subquery())
    total = session.exec(count_query).one()

    results = session.exec(query.offset(offset).limit(limit)).all()

    return total, list(results)


# Método para obtener un producto por id
def service_get_product_by_id(session: Session, prod_id: int) -> ProductReadFull:
    statement = (
        select(Product)
        .where(Product.id == prod_id)
        .options(selectinload(Product.categories))
    )

    product = session.exec(statement).first()

    if not product:
        raise ValueError("Producto no encontrado")

    return product


# Método para actualizar el total de un producto
def service_replace_product(
    session: Session, prod_id: int, data: ProductCreate
) -> ProductRead:
    product = session.get(Product, prod_id)

    if not product:
        raise ValueError("Producto no encontrado")

    for field, value in data.model_dump().items():
        setattr(product, field, value)

    product.updated_at = datetime.now(timezone.utc)

    session.add(product)
    session.commit()
    session.refresh(product)
    return ProductRead.model_validate(product)


# Método para actualizar parcialmente un producto
def service_update_product(
    session: Session, prod_id: int, data: ProductUpdate
) -> ProductRead:
    product = session.get(Product, prod_id)

    if not product:
        raise ValueError("Producto no encontrado")

    update_data = data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(product, field, value)

    product.updated_at = datetime.now(timezone.utc)

    session.add(product)
    session.commit()
    session.refresh(product)
    return ProductRead.model_validate(product)


# Método para manejar el borrado lógico
def service_toggle_product_status(session: Session, prod_id: int) -> ProductRead:
    product = session.get(Product, prod_id)

    if not product:
        raise ValueError("Producto no encontrado")

    product.available = not product.available
    product.deleted_at = None if product.available else datetime.now(timezone.utc)
    product.updated_at = datetime.now(timezone.utc)

    session.add(product)
    session.commit()
    session.refresh(product)
    return ProductRead.model_validate(product)


# Método para obtener el estado del stock de un producto
def service_get_stock_status(session: Session, prod_id: int) -> ProductStockResponse:
    product = session.get(Product, prod_id)

    if not product:
        raise ValueError("Producto no encontrado")

    stock_alert = product.stock < product.min_stock

    return ProductStockResponse(
        stock=product.stock,
        below_min_stock=stock_alert,
        available=product.available,
    )
