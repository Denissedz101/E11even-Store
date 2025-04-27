from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, date

# --- CLIENTE
class ClienteOut(BaseModel):
    rut: str
    nombre: str
    apellidos: str
    usuario: str
    email: str
    fechaNacimiento: date
    direccion: Optional[str] = None

    class Config:
        from_attributes = True

# --- PRODUCTO
class ProductoOut(BaseModel):
    id: int
    nombre: str
    descripcion: Optional[str] = None
    precio: int
    categoria: str
    imagen: str
    stock: int

    class Config:
        from_attributes = True

# --- DETALLE COMPRA
class DetalleCompraOut(BaseModel):
    producto_id: int
    cantidad: int

    class Config:
        from_attributes = True

# --- COMPRA
class CompraOut(BaseModel):
    id: int
    cliente_id: str 
    numero_compra: str
    direccion_envio: str
    metodo_pago: str
    fecha: datetime
    estado: str
    detalles: List[DetalleCompraOut] = []

    class Config:
        from_attributes = True
