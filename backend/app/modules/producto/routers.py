from fastapi import APIRouter, HTTPException, Path, Query, status, Body, Depends
from typing import Optional
from sqlmodel import Session

from .schemas import (
    ProductCreate,
    ProductRead,
    ProductUpdate,
    ProductStockResponse,
    ProductReadFull,
    ProductPaginatedResponse,
)
from . import services
from app.modules.producto_categoria import services as pc_services
from app.core.database import get_session

router = APIRouter(prefix="/productos", tags=["Productos"])


@router.post("/", response_model=ProductRead, status_code=status.HTTP_201_CREATED)
def create_product(
    data: ProductCreate = Body(...), session: Session = Depends(get_session)
):
    try:
        return services.service_create_product(session, data)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))


@router.get(
    "/", response_model=ProductPaginatedResponse, status_code=status.HTTP_200_OK
)
def get_all_products(
    session: Session = Depends(get_session),
    offset: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    name: Optional[str] = Query(None),
    available: Optional[bool] = Query(None),
):
    try:
        total, items = services.service_get_all_products(
            session, offset, limit, name, available
        )
        return ProductPaginatedResponse(total=total, items=items)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))


@router.get(
    "/{id}/stock", response_model=ProductStockResponse, status_code=status.HTTP_200_OK
)
def check_stock(id: int = Path(..., gt=0), session: Session = Depends(get_session)):
    try:
        return services.service_get_stock_status(session, id)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))


@router.get("/{id}", response_model=ProductReadFull, status_code=status.HTTP_200_OK)
def get_product_by_id(
    id: int = Path(..., gt=0), session: Session = Depends(get_session)
):
    try:
        return services.service_get_product_by_id(session, id)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))


@router.put("/{id}", response_model=ProductRead, status_code=status.HTTP_200_OK)
def replace_product(
    id: int = Path(..., gt=0),
    data: ProductCreate = Body(...),
    session: Session = Depends(get_session),
):
    try:
        return services.service_replace_product(session, id, data)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))


@router.patch("/{id}", response_model=ProductRead, status_code=status.HTTP_200_OK)
def update_product(
    id: int = Path(..., gt=0),
    data: ProductUpdate = Body(...),
    session: Session = Depends(get_session),
):
    try:
        return services.service_update_product(session, id, data)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))


@router.patch(
    "/{id}/desactivar", response_model=ProductRead, status_code=status.HTTP_200_OK
)
def toggle_product_status(
    id: int = Path(..., gt=0), session: Session = Depends(get_session)
):
    try:
        return services.service_toggle_product_status(session, id)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))


@router.post(
    "/{id}/categorias/{categoria_id}",
    response_model=ProductReadFull,
    status_code=status.HTTP_201_CREATED,
)
def assign_category(
    id: int = Path(..., gt=0),
    categoria_id: int = Path(..., gt=0),
    session: Session = Depends(get_session),
):
    try:
        return pc_services.service_assign_category(session, id, categoria_id)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))


@router.delete(
    "/{id}/categorias/{categoria_id}",
    response_model=ProductReadFull,
    status_code=status.HTTP_200_OK,
)
def remove_category(
    id: int = Path(..., gt=0),
    categoria_id: int = Path(..., gt=0),
    session: Session = Depends(get_session),
):
    try:
        return pc_services.service_remove_category(session, id, categoria_id)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))


@router.get(
    "/{id}/categorias", response_model=ProductReadFull, status_code=status.HTTP_200_OK
)
def get_categories_by_product(
    id: int = Path(..., gt=0),
    session: Session = Depends(get_session),
):
    try:
        return pc_services.service_get_categories_by_product(session, id)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))
