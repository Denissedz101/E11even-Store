from sqlalchemy import Column, Integer, String, Date
from pydantic import BaseModel
from typing import Optional


class ProductoOut(BaseModel):
    id: int
    nombre: str
    descripcion: Optional[str] = None

    class Config:
        from_attributes = True
