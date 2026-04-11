from sqlalchemy.orm import Session
from app.repositories.stock_movement_repository import StockMovementRepository
from app.models.stock_model import StockMovement
from app.services.product_service import ProductService
from app.schemas.product_schema import ProductUpdate


class StockMovementService:

    def __init__(self):
        self.repository_stock_movement = StockMovementRepository()
        self.product_service = ProductService()
        
    def input_movement(self, db: Session, product_id, amount,):

        if amount > 0:

            product = self.product_service.get_product(db, product_id)

            if  not product:
                raise ValueError("Produto não existe")
            
            now_amount = amount + product.quantidade

            update_data = ProductUpdate(quantidade=now_amount)
            self.product_service.update_product(db, product.id, update_data)
            
            movement = StockMovement(produto_id=product_id, tipo="entrada", quantidade=amount)

            self.repository_stock_movement.save_movement(db, movement)
        
        else:
            raise ValueError("Quantidade deve ser maior que zero")
        
        return {
            "message": "Movimentação de entrada realizada com sucesso",
            "product_id": str(product.id),
            "nova_quantidade": now_amount,
            "movimento": {
                    "tipo": movement.tipo,
                    "quantidade": movement.quantidade
                }
            }


    def output_movement(self, db: Session, product_id, amount,):

        if amount <= 0:
            raise ValueError("Quantidade deve ser maior que zero")
        
        product = self.product_service.get_product(db, product_id)
            
        if product.quantidade < amount:
            raise ValueError("Estoque insuficiente")

        now_amount = product.quantidade - amount

        update_data = ProductUpdate(quantidade=now_amount)
        self.product_service.update_product(db, product.id, update_data)
            
        movement = StockMovement(produto_id=product_id, tipo="saida", quantidade=amount)

        self.repository_stock_movement.save_movement(db, movement)
        
        
        return {
            "message": "Movimentação de saida realizada com sucesso",
            "product_id": str(product.id),
            "nova_quantidade": now_amount,
            "movimento": {
                    "tipo": movement.tipo,
                    "quantidade": movement.quantidade
                }
        }
    
