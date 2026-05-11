from fastapi import FastAPI
from app.routers.product_router import router as product_router
from app.routers.stock_movement_routers import router as stock_router
from app.routers.category_router import router as category_router
from app.models.product_model import Product
from app.models.stock_model import StockMovement
from app.models.category_model import Category
from contextlib import asynccontextmanager
from app.core.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware

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
    app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

    # Routers
    app.include_router(product_router, prefix="/api/v1", tags=["Products"])
    app.include_router(stock_router, prefix="/api/v1", tags=["Stok_Movement"])
    app.include_router(category_router, prefix="/api/v1", tags=["Categories"])
    

    return app


app = create_app()