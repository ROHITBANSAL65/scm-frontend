from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from crud import create_order, get_orders
from schemas import OrderSchema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/orders/")
def add_order(order: OrderSchema, db: Session = Depends(get_db)):
    return create_order(db, order)

@router.get("/orders/")
def list_orders(db: Session = Depends(get_db)):
    return get_orders(db)
