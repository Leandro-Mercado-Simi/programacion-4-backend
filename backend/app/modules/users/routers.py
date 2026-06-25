from fastapi import APIRouter, HTTPException, Path, status, Body, Depends
from typing import List
from . import schemas, services
from ...core.database import get_session
from sqlmodel import Session


router = APIRouter(prefix="/users", tags=["Usuarios"])


# Ruta estática para post
@router.post("/", response_model=schemas.UserRead, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, session: Session = Depends(get_session)):
    try:
        return services.service_create_user(session, user)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))


# Ruta estática para listar usuarios
@router.get("/", response_model=List[schemas.UserRead], status_code=status.HTTP_200_OK)
def get_all(session: Session = Depends(get_session)):
    try:
        return services.service_get_all_users(session)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))


# Ruta dinámica (con param) para obtener un usuario por id
@router.get("/{id}", response_model=schemas.UserRead, status_code=status.HTTP_200_OK)
def get_by_id(id: int = Path(..., gt=0), session: Session = Depends(get_session)):
    try:
        return services.service_get_user_by_id(session, id)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))


# Ruta dinámica para actualizar información de un usuario
@router.patch("/{id}", response_model=schemas.UserRead, status_code=status.HTTP_200_OK)
def update_user(
    id: int = Path(..., gt=0),
    user_data: schemas.UserUpdate = Body(
        ...,
    ),
    session: Session = Depends(get_session),
):
    try:
        return services.service_update_user(session, id, user_data)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))


# Ruta para cambiar el rol de un usuario específico
@router.patch(
    "/{id}/role/{role}", response_model=schemas.UserRead, status_code=status.HTTP_200_OK
)
def update_user_role(
    id: int = Path(..., gt=0),
    role: schemas.Role = Path(
        ...,
    ),
    session: Session = Depends(get_session),
):
    try:
        return services.service_change_role(session, id, role)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))


# Ruta dinámica para desactivar o reactivar usuarios
@router.patch(
    "/{id}/status", response_model=schemas.UserRead, status_code=status.HTTP_200_OK
)
def change_user_status(
    id: int = Path(..., gt=0), session: Session = Depends(get_session)
):
    try:
        return services.service_toggle_user_status(session, id)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))
