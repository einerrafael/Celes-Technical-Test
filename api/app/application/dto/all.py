from typing import Generic, TypeVar, List

from pydantic import BaseModel

Result = TypeVar('Result')


class PaginateDTO(BaseModel):
    page: int
    limit: int


class PaginatedResults(BaseModel, Generic[Result]):
    page: int
    total_pages: int
    total: int
    results: List[Result]
