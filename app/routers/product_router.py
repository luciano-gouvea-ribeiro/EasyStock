# app/routers/product_router.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.schemas.product_schema import ProductCreate, ProductUpdate, ProductResponse
from app.services.product_service import ProductService
from app.core.database import get_db


router = APIRouter(prefix="/products", tags=["Products"])
service = ProductService()


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