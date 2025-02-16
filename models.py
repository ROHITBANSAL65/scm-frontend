from sqlalchemy import Column, Integer, String
from database import Base

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, index=True)
    status = Column(String, default="Pending")

class Transport(Base):
    __tablename__ = "transports"
    id = Column(Integer, primary_key=True, index=True)
    driver_name = Column(String)
    vehicle_number = Column(String)
