from pydantic import BaseModel


class Employee(BaseModel):
    key: str
    code: str
    division: str
    name: str
    position: str
