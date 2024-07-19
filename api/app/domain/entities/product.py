from typing import Optional

from pydantic import BaseModel


class Product(BaseModel):
    key: Optional[str] = None
    code: Optional[str] = None
    sub_category_name: Optional[str] = None
    category_name: Optional[str] = None
    brand_name: Optional[str] = None
    name: Optional[str] = None
