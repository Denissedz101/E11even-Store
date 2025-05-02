from sqlalchemy.orm import Session
from . import models, schemas

def crear_cliente(db: Session, cliente: schemas.ClienteCreate):
    db_cliente = models.Cliente(**cliente.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def obtener_clientes(db: Session):
    return db.query(models.Cliente).all()

def crear_producto(db: Session, producto: schemas.ProductoCreate):
    db_producto = models.Producto(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def obtener_productos(db: Session):
    return db.query(models.Producto).all()

def get_compras(db: Session):
    return db.query(models.Compra).all()

def get_compras_by_rut(db: Session, rut: str):
    return db.query(models.Compra).filter(models.Compra.cliente_id == rut).all()

def get_detalles_by_compra(db: Session, compra_id: int):
    return db.query(models.DetalleCompra).filter(models.DetalleCompra.compra_id == compra_id).all()