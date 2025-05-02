from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# dependencias db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/clientes/", response_model=schemas.ClienteOut)
def crear_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    return crud.crear_cliente(db, cliente)

@app.get("/clientes/", response_model=list[schemas.ClienteOut])
def listar_clientes(db: Session = Depends(get_db)):
    return crud.obtener_clientes(db)
    
@app.get("/clientes/{rut}", response_model=schemas.ClienteBase)
def obtener_cliente(rut: str, db: Session = Depends(get_db)):
    cliente = crud.get_cliente(db, rut)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

@app.post("/productos/", response_model=schemas.ProductoOut)
def crear_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return crud.crear_producto(db, producto)

@app.get("/productos/", response_model=list[schemas.ProductoOut])
def listar_productos(db: Session = Depends(get_db)):
    return crud.obtener_productos(db)

@app.get("/productos/{id}", response_model=schemas.ProductoBase)
def obtener_producto(id: int, db: Session = Depends(get_db)):
    producto = crud.get_producto(db, id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@app.get("/compras", response_model=List[schemas.CompraBase])
def listar_compras(db: Session = Depends(get_db)):
    return crud.get_compras(db)

@app.get("/compras/{rut}", response_model=List[schemas.CompraBase])
def listar_compras_cliente(rut: str, db: Session = Depends(get_db)):
    return crud.get_compras_by_rut(db, rut)

@app.get("/detalles/{compra_id}", response_model=List[schemas.DetalleCompraBase])
def obtener_detalles(compra_id: int, db: Session = Depends(get_db)):
    return crud.get_detalles_by_compra(db, compra_id)
