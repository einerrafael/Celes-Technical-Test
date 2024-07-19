from typing import Optional

from pydantic import BaseModel


class Store(BaseModel):
    key: Optional[str] = None
    code: Optional[str] = None
    name: Optional[str] = None
    country: Optional[int] = None
    city: Optional[int] = None
    province: Optional[str] = None
    type: Optional[str] = None
