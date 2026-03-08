
import uuid
from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.core.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome = Column(String, nullable=False)
    sku = Column(String, unique=True, nullable=False)
    codigo_barras = Column(String, unique=True, nullable=True)

    preco_custo = Column(Float, nullable=False)
    preco_venda = Column(Float, nullable=False)

    quantidade = Column(Integer, default=0)
    estoque_minimo = Column(Integer, default=0)
    estoque_maximo = Column(Integer, nullable=True)

    ativo = Column(Boolean, default=True)

    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    atualizado_em = Column(DateTime(timezone=True), onupdate=func.now())