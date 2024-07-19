from typing import Optional

from pydantic import BaseModel


class StatisticTotAvg(BaseModel):
    key: Optional[str] = None
    count: Optional[int] = None
    avg: Optional[float] = None
    total: Optional[float] = None
