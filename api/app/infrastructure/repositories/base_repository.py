from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List, Tuple

T = TypeVar('T')
K = TypeVar('K')


class BaseRepository(ABC, Generic[T, K]):

    @abstractmethod
    def get_by_id(self, _id: K) -> Optional[T]:
        pass

    @abstractmethod
    def get_all(self, limit: int = None, offset: int = None) -> Tuple[Optional[List[T]], int]:
        pass
