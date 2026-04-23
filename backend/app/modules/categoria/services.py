from sqlmodel import Session, select
from typing import List
from .model import Category
from .schemas import CategoryCreate, CategoryUpdate


# Método para crear y persistir categorías
def service_create_category(
    session: Session,
    data: CategoryCreate,
) -> Category:
    category = Category.model_validate(data)

    session.add(category)
    session.commit()
    session.refresh(category)

    return category


# Método para listar todas las categorías guardadas en la bd
def service_get_all_categories(session: Session) -> List[Category]:
    statement = select(Category).where(Category.is_active == True)

    result = session.exec(statement)

    return result.all()


# Método para obtener una categoría por su id
def service_get_category_by_id(session: Session, category_id: int) -> Category:
    category = session.get(Category, category_id)

    if not category:
        raise ValueError("Categoría no encontrada")

    return category


# Método para actualizar una categoría
def service_update_category(
    session: Session, category_id: int, data: CategoryUpdate
) -> Category:
    category = session.get(Category, category_id)

    if not category:
        raise ValueError("Categoría no encontrada")

    update_data = data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(category, field, value)

    session.add(category)
    session.commit()
    session.refresh(category)

    return category


# Método para reemplazar una categoría
def service_replace_category(
    session: Session, category_id: int, data: CategoryCreate
) -> Category:
    category = session.get(Category, category_id)

    if not category:
        raise ValueError("Categoría no encontrada")

    for field, value in data.model_dump().items():
        setattr(category, field, value)

    session.add(category)
    session.commit()
    session.refresh(category)

    return category


# Método para borrado lógico de una categoría
def service_toggle_category_status(session: Session, category_id: int) -> Category:
    category = session.get(Category, category_id)

    if not category:
        raise ValueError("Categoría no encontrada")

    category.is_active = not category.is_active

    session.add(category)
    session.commit()
    session.refresh(category)

    return category
