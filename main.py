from fastapi import FastAPI
from app.routers.product_router import router as product_router
from app.models.product_model import Product
from app.models.stock_model import StockMovement
from contextlib import asynccontextmanager
from app.core.database import Base, engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

def create_app() -> FastAPI:
    app = FastAPI(
        title="EasyStock API",
        description="API para gerenciamento de estoque",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
        lifespan=lifespan
    )

    # Routers
    app.include_router(product_router, prefix="/api/v1", tags=["Products"])

    return app


app = create_app()