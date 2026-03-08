from sqlalchemy.orm import Session
from app.repositories.product_repository import ProductRepository
from app.schemas.product_schema import ProductCreate, ProductUpdate
from app.models.product_model import Product
from uuid import UUID


class ProductService:

    def __init__(self):
        self.repository = ProductRepository()

    def create_product(self, db: Session, product_data: ProductCreate) -> Product:

        
        if product_data.preco_venda < product_data.preco_custo:
            raise ValueError("Preço de venda não pode ser menor que o custo.")

        
        existing_products = self.repository.get_all(db)
        for product in existing_products:
            if product.sku == product_data.sku:
                raise ValueError("SKU já cadastrado.")

        return self.repository.create(db, product_data)

    def get_product(self, db: Session, product_id: UUID) -> Product:
        product = self.repository.get_by_id(db, product_id)

        if not product:
            raise ValueError("Produto não encontrado.")

        return product

    def list_products(self, db: Session):
        return self.repository.get_all(db)

    def update_product(self, db: Session, product_id: UUID, update_data: ProductUpdate):

        product = self.repository.get_by_id(db, product_id)

        if not product:
            raise ValueError("Produto não encontrado.")

        return self.repository.update(db, product, update_data)

    def delete_product(self, db: Session, product_id: UUID):

        product = self.repository.get_by_id(db, product_id)

        if not product:
            raise ValueError("Produto não encontrado.")

        self.repository.delete(db, product)