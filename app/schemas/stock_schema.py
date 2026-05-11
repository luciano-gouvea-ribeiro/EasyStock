from pydantic import BaseModel, Field


class MovementRequest(BaseModel):
    quantidade: int = Field(gt=0)
