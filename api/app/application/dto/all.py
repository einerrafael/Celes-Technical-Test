from typing import Generic, TypeVar, List, Any

from pydantic import BaseModel


class PaginateDTO(BaseModel):
    page: int
    limit: int


class PaginatedResults(BaseModel):
    page: int
    total_pages: int
    total: int
    results: List[Any]
