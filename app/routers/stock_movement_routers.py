from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.services.stock_movement_service import StockMovementService
from app.schemas.stock_schema import MovementRequest
from app.core.database import get_db


router = APIRouter(prefix="/products", tags=["Stok_Movement"])
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