# app/routers/product_router.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.schemas.product_schema import ProductCreate, ProductUpdate, ProductResponse
from app.services.product_service import ProductService
from app.core.database import get_db
from app.schemas.product_schema import MovementRequest
from app.services.stock_movement_service import StockMovementService


router = APIRouter(prefix="/products", tags=["Products"])
service = ProductService()
stock_service = StockMovementService()

@router.post("/{product_id}/entrada")
def input_movement(product_id: UUID, movement: MovementRequest,db: Session = Depends(get_db)):
    try:
        return stock_service.input_movement(db, product_id, movement.quantidade)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{product_id}/saida")
def output_movement(product_id: UUID,movement: MovementRequest, db: Session = Depends(get_db)):
    try:
        return stock_service.output_movement(db,product_id,movement.quantidade)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.post("/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    try:
        return service.create_product(db, product)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: UUID, db: Session = Depends(get_db)):
    try:
        return service.get_product(db, product_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/", response_model=list[ProductResponse])
def list_products(db: Session = Depends(get_db)):
    return service.list_products(db)


@router.put("/{product_id}", response_model=ProductResponse)
def update_product(product_id: UUID, update_data: ProductUpdate, db: Session = Depends(get_db)):
    try:
        return service.update_product(db, product_id, update_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{product_id}")
def delete_product(product_id: UUID, db: Session = Depends(get_db)):
    try:
        service.delete_product(db, product_id)
        return {"message": "Produto deletado com sucesso"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))