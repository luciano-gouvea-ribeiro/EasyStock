
from sqlalchemy.orm import Session
from app.repositories.category_repository import CategoryRepository
from app.schemas.category_schema import CategoryCreate, CategoryUpdate
from app.models.category_model import Category
from uuid import UUID


class CategoryService:

    def __init__(self):
        self.repository = CategoryRepository()

    def create_category(self, db: Session, category_data: CategoryCreate) -> Category:

        
        if not category_data.nome.strip():
            raise ValueError("Categoria do produto não pode estar vazia.")

        existing_category = self.repository.get_by_name(db, category_data.nome)
        if existing_category:
            raise ValueError("Categoria já cadastrada.")

        return self.repository.create(db, category_data)

    def get_category(self, db: Session, category_id: UUID) -> Category:
        category = self.repository.get_by_id(db, category_id)

        if not category or not category.ativo:
            raise ValueError("Categoria não encontrado.")

        return category

    def list_categories(self, db: Session):
        return self.repository.get_all(db)

    def update_category(self, db: Session, category_id: UUID, update_data: CategoryUpdate):

        category = self.repository.get_by_id(db, category_id)

        if not category or not category.ativo:
            raise ValueError("Categoria não encontrado, para fazer atualização")

        return self.repository.update(db, category, update_data)

    def delete_category(self, db: Session, category_id: UUID):

        category = self.repository.get_by_id(db, category_id)

        if not category or not category.ativo:
            raise ValueError("Categoria não encontrado, para deletar")

        return self.repository.delete(db, category)
