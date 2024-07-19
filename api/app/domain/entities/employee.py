from typing import Optional

from pydantic import BaseModel


class Employee(BaseModel):
    key: Optional[str] = None
    code: Optional[str] = None
    division: Optional[str] = None
    name: Optional[str] = None
    position: Optional[str] = None
