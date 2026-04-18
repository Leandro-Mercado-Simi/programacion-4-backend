from typing import List, Optional
from .schemas import UserCreate, UserRead, UserUpdate, Address, Role
from datetime import datetime, timezone

db_users: List[UserRead] = [
    UserRead(
        id=1,
        first_name="John",
        last_name="Doe",
        email="john.doe@mail.com",
        password="1234Abcd",
        phone="+5492611234567",
        address=Address(
            street="Av. San Martín 123",
            city="Mendoza",
            province="Mendoza",
            country="Argentina",
        ),
        role=Role.admin,
        registered_at=datetime(2026, 1, 20, 15, 30, tzinfo=timezone.utc),
        is_active=True,
    ),
    UserRead(
        id=2,
        first_name="María",
        last_name="Gonzalez",
        email="mgonzalez@mail.com",
        password="1234567A",
        phone="+5492611234567",
        address=Address(
            street="Av. Colón 256",
            city="Godoy Cruz",
            province="Mendoza",
            country="Argentina",
        ),
        role=Role.user,
        registered_at=datetime(2026, 2, 26, 15, 30, tzinfo=timezone.utc),
        is_active=True,
    ),
    UserRead(
        id=3,
        first_name="Juan",
        last_name="Perez",
        email="jperez@mail.com",
        password="Abcd1234",
        phone="+5492611234567",
        address=Address(
            street="Av. Santa Fe 4568",
            city="Maipú",
            province="Mendoza",
            country="Argentina",
        ),
        role=Role.client,
        registered_at=datetime(2026, 1, 15, 15, 30, tzinfo=timezone.utc),
        is_active=False,
    ),
]

id_user_counter = 4


# Método para crear un usuario nuevo
def create_user(user_data: UserCreate) -> UserRead:
    global id_user
    newUser = UserRead(id=id_user_counter, **user_data.model_dump())
    db_users.append(newUser)
    id_user_counter += 1
    return newUser


# Método para listar todos los usuarios que estén activos (que no hayan sido "borrados")
def get_all_users(skip: int = 0, limit: int = 10) -> List[UserRead]:
    active_users = [user for user in db_users if user.is_active]
    return active_users[skip : skip + limit]


# Método para obtener la información de un solo usuario por su id
def get_user_by_id(id: int) -> Optional[UserRead]:
    for user in db_users:
        if user.id == id:
            return user
    return None


# Método para actualizar la información de un usuario
def update_user_data(id: int, user_data: UserUpdate) -> Optional[UserRead]:
    for index, user in enumerate(db_users):
        if user.id == id:
            updated_user = UserRead(id=id, **user_data.model_dump())
            db_users[index] = updated_user
            return updated_user
    return None


# Método para cambiar el rol de un usuario admin | user | client
def change_role(id: int, role: Role) -> Optional[UserRead]:
    for index, user in enumerate(db_users):
        if user.id == id:
            user_dict = user.model_dump()
            user_dict["role"] = role
            updatedUser = UserRead(**user_dict)
            db_users[index] = updatedUser
            return updatedUser
    return None


# Método borrado lógico para ocultar usuarios
def toggle_user_status(id: int, status: bool) -> Optional[UserRead]:
    for index, user in enumerate(db_users):
        if user.id == id:
            user_dict = user.model_dump()
            user_dict["is_active"] = status
            updated_user = UserRead(**user_dict)
            db_users[index] = updated_user
            return updated_user
    return None
