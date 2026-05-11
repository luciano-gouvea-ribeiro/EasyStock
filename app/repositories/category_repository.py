from sqlalchemy.orm import Session
from app.models.category_model import Category
from uuid import UUID
from app.schemas.category_schema import CategoryCreate, CategoryUpdate

class CategoryRepository:

    def create(self, db: Session, category_data: CategoryCreate) -> Category:
        category = Category(**category_data.dict())
        db.add(category)
        db.commit()
        db.refresh(category)
        return category

    def get_by_id(self, db: Session, category_id: UUID) -> Category | None:
        return db.query(Category).filter(Category.id == category_id).first()

    def get_all(self, db: Session) -> Category:
        return db.query(Category).filter(Category.ativo == True).all()
    
    def get_by_name(self, db: Session, category_name: str) -> Category | None:
        return db.query(Category).filter(Category.ativo == True).filter(Category.nome == category_name).first()

    def update(self, db: Session, category: Category, update_data: CategoryUpdate) -> Category:
        for key, value in update_data.dict(exclude_unset=True).items():
            setattr(category, key, value)

        db.commit()
        db.refresh(category)
        return category

    def delete(self, db: Session, category: Category) -> Category:

        category.ativo = False
        db.commit()
        db.refresh(category)
        return category