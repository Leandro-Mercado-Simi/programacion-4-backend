from sqlmodel import Session, select
from .model import User
from typing import List
from .schemas import UserCreate, UserUpdate, Role
from ...utils.utils import hash_password


# Método para persistir un nuevo usuario
def service_create_user(session: Session, data: UserCreate) -> User:
    user = User.model_validate(data)

    user.password = hash_password(user.password)
    session.add(user)
    session.commit()
    session.refresh(user)

    return user


# Método para obtener la información de un solo usuario por su id
def service_get_user_by_id(session: Session, user_id: int) -> User:
    user = session.get(User, user_id)

    if not user:
        raise ValueError("Usuario no encontrado")

    return user


# Método para listar todos los usuarios que estén activos (que no hayan sido "borrados")
def service_get_all_users(session: Session) -> List[User]:
    statement = select(User).where(User.is_active == True)

    result = session.exec(statement)

    return result.all()


# Método para actualizar la información de un usuario
def service_update_user(session: Session, user_id: int, user_data: UserUpdate) -> User:
    user = session.get(User, user_id)

    if not user:
        raise ValueError("Usuario no encontrado")

    updated_data = user_data.model_dump(exclude_unset=True)

    for field, value in updated_data.items():
        setattr(user, field, value)

    session.add(user)
    session.commit()
    session.refresh(user)
    return user


# Método para cambiar el rol de un usuario admin | user | client
def service_change_role(session: Session, user_id: int, role: Role) -> User:
    user = session.get(User, user_id)

    if not user:
        raise ValueError("Usuario no encontrado")

    user.role = role

    session.add(user)
    session.commit()
    session.refresh(user)
    return user


# Método borrado lógico para ocultar usuarios
def service_toggle_user_status(session: Session, user_id: int) -> User:
    user = session.get(User, user_id)

    if not user:
        raise ValueError("Usuario no encontrado")

    user.is_active = not user.is_active

    session.add(user)
    session.commit()
    session.refresh(user)

    return user
