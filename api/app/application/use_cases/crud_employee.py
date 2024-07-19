from math import ceil

from app.application.dto.all import PaginateDTO, PaginatedResults
from app.domain.repositories import EmployeeRepository


class CRUDEmployee:

    def __init__(self,
                 employee_repository: EmployeeRepository):
        self.__employee_repository = employee_repository

    def all_employees(self, paginate: PaginateDTO) -> PaginatedResults:
        _all, total = self.__employee_repository.get_all(paginate.limit, offset=(paginate.page - 1) * paginate.limit)
        return PaginatedResults(
            page=paginate.page,
            total_pages=ceil(total / paginate.limit),
            total=total,
            results=_all
        )
