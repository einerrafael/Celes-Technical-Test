from enum import Enum
from typing import Generic, TypeVar, List, Any, Optional

from pydantic import BaseModel


class PaginateDTO(BaseModel):
    page: int
    limit: int


class PaginatedResults(BaseModel):
    page: int
    total_pages: int
    total: int
    results: List[Any]


class ResponseMessageCode(str, Enum):
    EMPTY_RESULTS = "EMPTY_RESULTS"
    FATAL_ERROR = "FATAL_ERROR"


class ResponseStatus(str, Enum):
    ERROR = "ERROR"
    INFO = "INFO"
    WARNING = "WARNING"


class ResponseMessage(BaseModel):
    code: ResponseMessageCode
    status: ResponseStatus
    message: Optional[str]
