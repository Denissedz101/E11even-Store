from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine
from typing import List
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.title ="E11even Store"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8001", "http://localhost:8001"],
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    cliente = db.query(models.Cliente).filter(models.Cliente.rut == rut).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

@app.post("/productos/", response_model=schemas.ProductoOut)
def crear_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return crud.crear_producto(db, producto)

@app.get("/productos/", response_model=list[schemas.ProductoOut])
def listar_productos(db: Session = Depends(get_db)):
    return crud.obtener_productos(db)

@app.get("/productos/{categoria}", response_model=List[schemas.ProductoOut])
def obtener_productos_categoria(categoria: str, db: Session = Depends(get_db)):
    productos = crud.obtener_productos_por_categoria(db, categoria)
    if not productos:
        raise HTTPException(status_code=404, detail="No se encontraron productos en esta categoría")
    return productos

@app.get("/compras", response_model=List[schemas.CompraBase])
def listar_compras(db: Session = Depends(get_db)):
    return crud.obtener_compras(db)

@app.get("/compras/{rut}", response_model=List[schemas.CompraBase])
def listar_compras_cliente(rut: str, db: Session = Depends(get_db)):
    return crud.obtener_compras_by_rut(db, rut)

@app.get("/detalles/{compra_id}", response_model=List[schemas.DetalleCompraBase])
def obtener_detalles(compra_id: int, db: Session = Depends(get_db)):
    return crud.obtener_detalles_by_compra(db, compra_id)


