from sqlalchemy import Column, String, Integer, Date, Text
from .database import Base


# PRODUCTO
class Producto(Base):
    __tablename__ = "E11EVENSTORE_PRODUCTO"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))
    descripcion = Column(String(500), nullable=True)
    precio = Column(Integer)
    categoria = Column(String(50))
    imagen = Column(String(2000))
    stock = Column(Integer)
