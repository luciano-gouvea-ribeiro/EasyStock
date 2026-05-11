from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional



class CategoryCreate(BaseModel):
    nome: str 
    descricao: Optional[str] = None

    
class CategoryUpdate(BaseModel):
    nome: Optional[str] = None 
    descricao: Optional[str] = None
    ativo: Optional[bool] = None

class CategoryResponse(BaseModel):
    id: UUID
    nome: str
    descricao: Optional[str] = None
    ativo: bool
    criado_em: datetime
    atualizado_em: Optional[datetime]
    
    class Config:
        from_attributes = True
    