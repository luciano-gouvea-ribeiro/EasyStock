from sqlalchemy.orm import Session
from app.models.stock_model import StockMovement


class StockMovementRepository:

    def save_movement(self, db: Session, movement: StockMovement) -> StockMovement:
        db.add(movement)
        db.commit()
        db.refresh(movement)
        return movement