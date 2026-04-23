from fastapi import FastAPI
from contextlib import asynccontextmanager
from .database.database import create_table_db
from .modules.producto.routers import router as producto_router
from .modules.categoria.routers import router as categoria_router
from .modules.users.routers import router as usuarios_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_table_db()
    yield


def create_app() -> FastAPI:
    app = FastAPI(
        title="API Integradora - Unidad 2",
        description="Conceptos: Persistencia",
        version="2.0.0",
        lifespan=lifespan,
    )

    app.include_router(producto_router)
    app.include_router(categoria_router)
    app.include_router(usuarios_router)

    return app


app = create_app()


@app.get("/")
def root():
    return "server prendido"
