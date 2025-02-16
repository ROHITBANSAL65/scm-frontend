from pydantic import BaseModel

class OrderSchema(BaseModel):
    customer_name: str
    status: str = "Pending"

class TransportSchema(BaseModel):
    driver_name: str
    vehicle_number: str
