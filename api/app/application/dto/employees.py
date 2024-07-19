from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.application.dto.all import PaginateDTO


class SalesEmployeeFilterDTO(BaseModel):
    employee_id: str
    pagination: PaginateDTO
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
