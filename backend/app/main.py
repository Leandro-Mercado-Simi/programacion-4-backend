from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.core.database import create_table_db
from app.modules.producto.routers import router as producto_router
from app.modules.categoria.routers import router as categoria_router
from app.modules.users.routers import router as usuarios_router

from app.modules.categoria.model import Category
from app.modules.producto.model import Product
from app.modules.producto_categoria.model import ProductCategoryLink


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_table_db()
    yield


def create_app() -> FastAPI:
    app = FastAPI(
        title="API Integradora - Unidad 3",
        description="Conceptos: CRUD Categorías - CRUD Productos",
        version="2.0.0",
        lifespan=lifespan,
    )

    app.include_router(producto_router)
    app.include_router(categoria_router)
    app.include_router(usuarios_router)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


app = create_app()


@app.get("/")
def root():
    return "server prendido"
