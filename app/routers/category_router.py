from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.schemas.category_schema import CategoryCreate, CategoryUpdate, CategoryResponse
from app.services.category_service import CategoryService
from app.core.database import get_db


router = APIRouter(prefix="/categories", tags=["Categories"])
service = CategoryService()


@router.post("/", response_model=CategoryResponse)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    try:
        return service.create_category(db, category)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(category_id: UUID, db: Session = Depends(get_db)):
    try:
        return service.get_category(db, category_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/", response_model=list[CategoryResponse])
def list_categories(db: Session = Depends(get_db)):
    return service.list_categories(db)


@router.put("/{category_id}", response_model=CategoryResponse)
def update_category(category_id: UUID, update_data: CategoryUpdate, db: Session = Depends(get_db)):
    try:
        return service.update_category(db, category_id, update_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{category_id}")
def delete_category(category_id: UUID, db: Session = Depends(get_db)):
    try:
        service.delete_category(db, category_id)
        return {"message": "Categoria deletada com sucesso"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))