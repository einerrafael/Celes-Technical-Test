from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.application.dto.all import PaginateDTO


class FilterDateRangesDTOWithPag(BaseModel):
    pagination: PaginateDTO
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None


class SalesEmployeeFilterDTO(FilterDateRangesDTOWithPag, BaseModel):
    employee_id: str


class SalesProductFilterDTO(FilterDateRangesDTOWithPag, BaseModel):
    product_id: str


class SalesStoreFilterDTO(FilterDateRangesDTOWithPag, BaseModel):
    store_id: str
