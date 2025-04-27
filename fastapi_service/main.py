from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Cliente, Producto, Compra
from .schemas import ClienteOut, ProductoOut, CompraOut

app = FastAPI()

# Dependencia de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- ENDPOINTS
@app.get("/clientes", response_model=list[ClienteOut])
def listar_clientes(db: Session = Depends(get_db)):
    return db.query(Cliente).all()

@app.get("/productos", response_model=list[ProductoOut])
def listar_productos(db: Session = Depends(get_db)):
    return db.query(Producto).all()

@app.get("/compras", response_model=list[CompraOut])
def listar_compras(db: Session = Depends(get_db)):
    return db.query(Compra).all()
