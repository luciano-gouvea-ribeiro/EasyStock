from sqlalchemy.orm import Session
from app.models.product_model import Product
from app.schemas.product_schema import ProductCreate, ProductUpdate
from uuid import UUID

class ProductRepository:

    def create(self, db: Session, product_data: ProductCreate) -> Product:
        product = Product(**product_data.dict())
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    def get_by_id(self, db: Session, product_id: UUID) -> Product | None:
        return db.query(Product).filter(Product.id == product_id).first()

    def get_all(self, db: Session):
        return db.query(Product).filter(Product.ativo == True).all()

    def update(self, db: Session, product: Product, update_data: ProductUpdate):
        for key, value in update_data.dict(exclude_unset=True).items():
            setattr(product, key, value)

        db.commit()
        db.refresh(product)
        return product
    
    def get_by_name(self, db:Session, product_name: str):
        return db.query(Product).filter(Product.nome.ilike(f"%{product_name}%")).filter(Product.ativo == True).all()
    
    def get_by_sku(self, db:Session, product_sku: str):
        return db.query(Product).filter(Product.sku == product_sku).filter(Product.ativo == True).all()

    def delete(self, db: Session, product: Product):

        product.ativo = False
        db.commit()

    def paginate_products(self, db:Session, page: int, limit: int):
      offset = (page - 1) * limit
      return db.query(Product).filter(Product.ativo == True).offset(offset).limit(limit).all()

    