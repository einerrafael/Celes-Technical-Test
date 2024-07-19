from math import ceil
from typing import Optional

from app.application.dto.all import PaginateDTO, PaginatedResults
from app.domain.entities.product import Product
from app.domain.repositories import ProductRepository
from app.infrastructure.api.statuses import ResultsNotFound


class CRUDProduct:

    def __init__(self,
                 product_repository: ProductRepository):
        self.__product_repository = product_repository

    def get_by_id(self, _id: str) -> Optional[Product]:
        result = self.__product_repository.get_by_id(_id)

        if result is None:
            raise ResultsNotFound()

        return result

    def all_products(self, paginate: PaginateDTO) -> PaginatedResults:
        _all, total = self.__product_repository.get_all(paginate.limit, offset=(paginate.page - 1) * paginate.limit)
        return PaginatedResults(
            page=paginate.page,
            total_pages=ceil(total / paginate.limit),
            total=total,
            results=_all
        )
