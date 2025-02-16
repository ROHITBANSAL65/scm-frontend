from sqlalchemy.orm import Session
from models import Order, Transport
from schemas import OrderSchema, TransportSchema

def create_order(db: Session, order: OrderSchema):
    new_order = Order(**order.dict())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

def get_orders(db: Session):
    return db.query(Order).all()
