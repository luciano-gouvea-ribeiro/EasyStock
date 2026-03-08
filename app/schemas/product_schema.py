from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from typing import Optional


class ProductBase(BaseModel):
    nome: str = Field(..., min_length=3, max_length=100)
    sku: str = Field(..., min_length=3, max_length=50)
    codigo_barras: Optional[str] = None

    preco_custo: float = Field(..., gt=0)
    preco_venda: float = Field(..., gt=0)

    quantidade: int = Field(default=0, ge=0)
    estoque_minimo: int = Field(default=0, ge=0)
    estoque_maximo: Optional[int] = None

    ativo: bool = True

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    nome: Optional[str] = None
    preco_venda: Optional[float] = None
    quantidade: Optional[int] = None
    estoque_minimo: Optional[int] = None
    estoque_maximo: Optional[int] = None
    ativo: Optional[bool] = None

class ProductResponse(ProductBase):
    id: UUID
    criado_em: datetime
    atualizado_em: Optional[datetime]

    class Config:
        from_attributes = True