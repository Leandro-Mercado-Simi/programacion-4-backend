from fastapi import APIRouter, HTTPException, Path, Query, status, Body, Depends
from typing import Optional
from sqlmodel import Session

from .schemas import (
    CategoryCreate,
    CategoryRead,
    CategoryUpdate,
    CategoryReadFull,
    CategoryPaginatedResponse,
)
from . import services
from app.modules.producto_categoria import services as pc_services
from app.core.database import get_session

router = APIRouter(prefix="/categorias", tags=["Categorías"])


# Ruta estática POST para crear una categoría
@router.post("/", response_model=CategoryRead, status_code=status.HTTP_201_CREATED)
def create_category(
    category: CategoryCreate = Body(...),
    session: Session = Depends(get_session),
):
    try:
        return services.service_create_category(session, category)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))


# Ruta estática GET Para obtener el listado de categorías
@router.get(
    "/", response_model=CategoryPaginatedResponse, status_code=status.HTTP_200_OK
)
def get_all_categories(
    session: Session = Depends(get_session),
    offset: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    name: Optional[str] = Query(None),
    is_active: Optional[bool] = Query(None),
):
    try:
        total, items = services.service_get_all_categories(
            session, offset, limit, name, is_active
        )
        return CategoryPaginatedResponse(total=total, items=items)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))


# Ruta dinámica GET para obtener la información de una categoría por id
@router.get("/{id}", response_model=CategoryReadFull, status_code=status.HTTP_200_OK)
def get_category_by_id(
    id: int = Path(..., gt=0), session: Session = Depends(get_session)
):
    try:
        return services.service_get_category_by_id(session, id)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))


# Ruta dinámica PUT para actualizar la totalidad de la data de una categoría
@router.put("/{id}", response_model=CategoryRead, status_code=status.HTTP_200_OK)
def replace_category(
    id: int = Path(..., gt=0),
    data: CategoryCreate = Body(...),
    session: Session = Depends(get_session),
):
    try:
        return services.service_replace_category(session, id, data)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))


# Ruta dinámica PATCH para actualizar información parcial de una categoría
@router.patch("/{id}", response_model=CategoryRead, status_code=status.HTTP_200_OK)
def update_category(
    id: int = Path(..., gt=0),
    data: CategoryUpdate = Body(...),
    session: Session = Depends(get_session),
):
    try:
        return services.service_update_category(session, id, data)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))


# Ruta dinámica PATCH para manejar el borrado lógico de una categoría
@router.patch(
    "/{id}/desactivar",
    response_model=CategoryRead,
    status_code=status.HTTP_200_OK,
)
def change_category_status(
    id: int = Path(..., gt=0), session: Session = Depends(get_session)
):
    try:
        return services.service_toggle_category_status(session, id)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))


# Endpoint para obtener una categoría con los productos que pertenecen a la misma
@router.get(
    "/{id}/productos", response_model=CategoryReadFull, status_code=status.HTTP_200_OK
)
def get_products_by_category(
    id: int = Path(..., gt=0),
    session: Session = Depends(get_session),
):
    try:
        return pc_services.service_get_products_by_category(session, id)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))
