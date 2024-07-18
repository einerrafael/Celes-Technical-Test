from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List

T = TypeVar('T')
K = TypeVar('K')


class BaseRepository(ABC, Generic[T, K]):

    @abstractmethod
    def create(self, _new: T) -> Optional[K]:
        pass

    @abstractmethod
    def get_by_id(self, _id: K) -> Optional[T]:
        pass

    @abstractmethod
    def get_all(self) -> Optional[List[T]]:
        pass

    @abstractmethod
    def filter(self, **kwargs) -> Optional[List[T]]:
        pass

    @abstractmethod
    def non_query(self, **kwargs) -> Optional[List[T]]:
        pass
