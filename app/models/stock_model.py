import uuid
from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.core.database import Base
from datetime import datetime


class StockMovement(Base):
    __tablename__ = "stock_movements"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    produto_id = Column(UUID, nullable=False)
    tipo = Column(String, nullable=False)
    quantidade = Column(Integer)
    data = Column(DateTime, default=datetime.utcnow)