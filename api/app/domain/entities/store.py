from pydantic import BaseModel


class Store(BaseModel):
    key: str
    code: str
    name: str
    country: int
    city: int
    province: str
    type: str
