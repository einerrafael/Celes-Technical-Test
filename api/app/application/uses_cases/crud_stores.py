from math import ceil
from typing import Optional

from app.application.dto.all import PaginateDTO, PaginatedResults
from app.domain.entities.store import Store
from app.domain.repositories import StoreRepository
from app.infrastructure.api.statuses import ResultsNotFound


class CRUDStores:

    def __init__(self,
                 stores_repository: StoreRepository):
        self.__stores_repository = stores_repository

    def get_by_id(self, _id: str) -> Optional[Store]:
        result = self.__stores_repository.get_by_id(_id)

        if result is None:
            raise ResultsNotFound()

        return result

    def all(self, paginate: PaginateDTO) -> PaginatedResults:
        _all, total = self.__stores_repository.get_all(paginate.limit, offset=(paginate.page - 1) * paginate.limit)
        return PaginatedResults(
            page=paginate.page,
            total_pages=ceil(total / paginate.limit),
            total=total,
            results=_all
        )
