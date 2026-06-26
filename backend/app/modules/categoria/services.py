from sqlmodel import Session, select, func
from typing import List, Optional, Tuple
from sqlalchemy.orm import selectinload
from datetime import datetime, timezone

from .model import Category
from .schemas import CategoryCreate, CategoryUpdate, CategoryRead, CategoryReadFull


# Método para crear y persistir categorías
def service_create_category(session: Session, data: CategoryCreate) -> CategoryRead:
    category = Category.model_validate(data)

    session.add(category)
    session.commit()
    session.refresh(category)

    return CategoryRead.model_validate(category)


# Método para listar todas las categorías guardadas en la bd
def service_get_all_categories(
    session: Session,
    offset: int = 0,
    limit: int = 20,
    name: Optional[str] = None,
    is_active: Optional[bool] = None,
) -> Tuple[int, List[Category]]:
    query = select(Category).options(selectinload(Category.products))

    if name:
        query = query.where(Category.name.ilike(f"%{name}%"))        
    if is_active is not None:
        query = query.where(Category.is_active == is_active)

    count_query = select(func.count()).select_from(query.subquery())
    total = session.exec(count_query).one()

    results = session.exec(query.offset(offset).limit(limit)).all()

    return total, list(results)


# Método para obtener una categoría por su id
def service_get_category_by_id(session: Session, category_id: int) -> CategoryReadFull:
    statement = (
        select(Category)
        .where(Category.id == category_id)
        .options(selectinload(Category.products))
    )

    category = session.exec(statement).first()

    if not category:
        raise ValueError("Categoría no encontrada")

    return category


# Método para actualizar una categoría
def service_update_category(
    session: Session, category_id: int, data: CategoryUpdate
) -> CategoryRead:
    category = session.get(Category, category_id)

    if not category:
        raise ValueError("Categoría no encontrada")

    update_data = data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(category, field, value)

    category.updated_at = datetime.now(timezone.utc)

    session.add(category)
    session.commit()
    session.refresh(category)
    return CategoryRead.model_validate(category)


# Método para reemplazar una categoría
def service_replace_category(
    session: Session, category_id: int, data: CategoryCreate
) -> CategoryRead:
    category = session.get(Category, category_id)

    if not category:
        raise ValueError("Categoría no encontrada")

    for field, value in data.model_dump().items():
        setattr(category, field, value)

    category.updated_at = datetime.now(timezone.utc)

    session.add(category)
    session.commit()
    session.refresh(category)
    return CategoryRead.model_validate(category)


# Método para borrado lógico de una categoría
def service_toggle_category_status(session: Session, category_id: int) -> CategoryRead:
    category = session.get(Category, category_id)

    if not category:
        raise ValueError("Categoría no encontrada")

    category.is_active = not category.is_active
    category.deleted_at = None if category.is_active else datetime.now(timezone.utc)
    category.updated_at = datetime.now(timezone.utc)

    session.add(category)
    session.commit()
    session.refresh(category)
    return CategoryRead.model_validate(category)
