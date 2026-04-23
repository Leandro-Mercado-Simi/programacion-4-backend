from fastapi import APIRouter, HTTPException, Path, status, Body, Depends
from typing import List
from .schemas import ProductCreate, ProductRead, ProductUpdate, ProductStockResponse
from . import services
from ...database.database import get_session
from sqlmodel import Session

router = APIRouter(prefix="/productos", tags=["Productos"])


# ---------------------------------------------------------
# ALTA DE PRODUCTO
# Método: POST | Endpoint: /productos | Estado: 201 Created
# Ruta estática POST para crear un nuevo producto
# ---------------------------------------------------------
@router.post("/", response_model=ProductRead, status_code=status.HTTP_201_CREATED)
def create_product(data: ProductCreate, session: Session = Depends(get_session)):
    try:
        return services.service_create_product(session, data)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))


# (Extra) LISTAR PRODUCTOS
# Ruta estática GET para obtener una lista de todos los productos
@router.get("/", response_model=List[ProductRead], status_code=status.HTTP_200_OK)
def get_all_products(session: Session = Depends(get_session)):
    try:
        return services.service_get_all_products(session)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))


# ---------------------------------------------------------
# CONSULTAR STOCK (Lógica de Negocio)
# Método: GET | Endpoint: /productos/{id}/stock | Estado: 200 OK
# Ruta dinámica GET Para obtener el estado del stock de un producto por su ID
# ---------------------------------------------------------
@router.get(
    "/{id}/stock",
    response_model=ProductStockResponse,
    status_code=status.HTTP_200_OK,
)
def check_stock(id: int = Path(..., gt=0), session: Session = Depends(get_session)):
    try:
        return services.service_get_stock_status(session, id)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))


# ---------------------------------------------------------
# DETALLE DE PRODUCTO
# Método: GET | Endpoint: /productos/{id} | Estado: 200 OK
# Ruta dinámica GET para obtener la información de un producto por su ID
# ---------------------------------------------------------
@router.get("/{id}", response_model=ProductRead, status_code=status.HTTP_200_OK)
def get_product_by_id(
    id: int = Path(..., gt=0), session: Session = Depends(get_session)
):
    try:
        return services.service_get_product_by_id(session, id)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))


# ---------------------------------------------------------
# ACTUALIZACIÓN (Reemplazo Total)
# Método: PUT | Endpoint: /productos/{id} | Estado: 200 OK
# Ruta dinámica PUT para actualizar el total de la información de un producto
# ---------------------------------------------------------
@router.put("/{id}", response_model=ProductRead, status_code=status.HTTP_200_OK)
def replace_product(
    id: int = Path(..., gt=0),
    data: ProductCreate = Body(
        ...,
    ),
    session: Session = Depends(get_session),
):
    try:
        return services.service_replace_product(session, id, data)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))


# Ruta dinámica PATCH para actualizar parcialmente un producto
@router.patch("/{id}", response_model=ProductRead, status_code=status.HTTP_200_OK)
def update_product(
    id: int = Path(..., gt=0),
    data: ProductUpdate = Body(
        ...,
    ),
    session: Session = Depends(get_session),
):
    try:
        return services.service_update_product(session, id, data)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))


# ---------------------------------------------------------
# BORRADO LÓGICO
# Método: PATCH | Endpoint: /productos/{id}/desactivar | Estado: 200 OK
# Ruta dinámica patch para cambiar el estado de un producto (Borrado lógico)
# ---------------------------------------------------------
@router.patch(
    "/{id}/desactivar",
    response_model=ProductRead,
    status_code=status.HTTP_200_OK,
)
def toggle_product_status(
    id: int = Path(..., gt=0), session: Session = Depends(get_session)
):
    try:
        return services.service_toggle_product_status(session, id)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))
