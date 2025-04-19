from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Producto, Administrativo
from .schemas import ProductoOut, AdministrativoOut

app = FastAPI(debug=True)


# Dependencia de DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Endpoint Productos
@app.get("/productos", response_model=list[ProductoOut])
def listar_productos(db: Session = Depends(get_db)):
    return db.query(Producto).all()
