from fastapi import APIRouter, HTTPException, Path, Query, status, Body
from typing import List
from . import schemas, services

router = APIRouter(prefix="/users", tags=["Usuarios"])


# Ruta estática para post
@router.post("/", response_model=schemas.UserRead, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate):
    return services.create_user(user)


# Ruta estática para listar usuarios
@router.get("/", response_model=List[schemas.UserRead], status_code=status.HTTP_200_OK)
def get_all(skip: int = Query(0, ge=0), limit: int = Query(10, le=50)):
    return services.get_all_users(skip, limit)


# Ruta dinámica (con param) para obtener un usuario por id
@router.get("/{id}", response_model=schemas.UserRead, status_code=status.HTTP_200_OK)
def get_by_id(id: int = Path(..., gt=0)):
    user = services.get_user_by_id(id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="usuario no encontrado",
        )
    return user


# Ruta dinámica para actualizar información de un usuario
@router.patch("/{id}", response_model=schemas.UserRead, status_code=status.HTTP_200_OK)
def update_user(
    id: int = Path(..., gt=0),
    user_data: schemas.UserUpdate = Body(
        ...,
    ),
):
    updated_user = services.update_user_data(id, user_data)
    if not updated_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuario con id {id} no encontrado",
        )
    return updated_user


# Ruta para cambiar el rol de un usuario específico
@router.patch(
    "/{id}/role/{role}", response_model=schemas.UserRead, status_code=status.HTTP_200_OK
)
def update_user_role(
    id: int = Path(..., gt=0),
    role: schemas.Role = Path(
        ...,
    ),
):
    updated_user = services.change_role(id, role)
    if not updated_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuario con id {id} no encontrado",
        )
    return updated_user


# Ruta dinámica para desactivar o reactivar usuarios
@router.patch(
    "/{id}/status", response_model=schemas.UserRead, status_code=status.HTTP_200_OK
)
def change_user_status(
    id: int = Path(..., gt=0),
    is_active: bool = Query(
        ...,
    ),
):
    modified_user = services.toggle_user_status(id, is_active)
    if not modified_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuario con id {id} no encontrado",
        )
    return modified_user
