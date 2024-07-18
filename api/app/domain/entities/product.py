from pydantic import BaseModel


class Product(BaseModel):
    key: str
    code: str
    sub_category_name: str
    category_name: str
    brand_name: str
    name: str
