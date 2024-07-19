from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.domain.entities.product import Product


class Sale(BaseModel):
    key: Optional[str] = None
    date: Optional[datetime] = None
    store_key: Optional[str] = None
    customer_key: Optional[str] = None
    product_key: Optional[str] = None
    product: Optional[Product] = None
    amount: Optional[float] = None
    ticket_key: Optional[str] = None


class Employee(BaseModel):
    key: Optional[str] = None
    code: Optional[str] = None
    division: Optional[str] = None
    name: Optional[str] = None
    position: Optional[str] = None
