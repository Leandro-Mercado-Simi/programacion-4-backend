from sqlmodel import Session, select
from sqlalchemy.orm import selectinload
from typing import Optional, List

from .model import ProductCategoryLink
from app.modules.producto.model import Product
from app.modules.categoria.model import Category


def service_assign_category(
    session: Session, product_id: int, category_id: int
) -> Product:
    product = session.get(Product, product_id)
    category = session.get(Category, category_id)

    if not product:
        raise ValueError("Producto no encontrado")
    if not category:
        raise ValueError("Categoría no encontrada")

    existing = session.exec(
        select(ProductCategoryLink).where(
            ProductCategoryLink.product_id == product_id,
            ProductCategoryLink.category_id == category_id,
        )
    ).first()

    if existing:
        raise ValueError("El producto ya tiene asignada esa categoría")

    link = ProductCategoryLink(product_id=product_id, category_id=category_id)
    session.add(link)
    session.commit()

    return session.exec(
        select(Product)
        .where(Product.id == product_id)
        .options(selectinload(Product.categories))
    ).first()


def service_remove_category(
    session: Session, product_id: int, category_id: int
) -> Product:
    link = session.exec(
        select(ProductCategoryLink).where(
            ProductCategoryLink.product_id == product_id,
            ProductCategoryLink.category_id == category_id,
        )
    ).first()

    if not link:
        raise ValueError("Vínculo no encontrado")

    session.delete(link)
    session.commit()

    return session.exec(
        select(Product)
        .where(Product.id == product_id)
        .options(selectinload(Product.categories))
    ).first()


def service_get_categories_by_product(session: Session, product_id: int) -> Product:
    product = session.exec(
        select(Product)
        .where(Product.id == product_id)
        .options(selectinload(Product.categories))
    ).first()

    if not product:
        raise ValueError("Producto no encontrado")

    return product


def service_get_products_by_category(session: Session, category_id: int) -> Category:
    category = session.exec(
        select(Category)
        .where(Category.id == category_id)
        .options(selectinload(Category.products))
    ).first()

    if not category:
        raise ValueError("Categoría no encontrada")

    return category
