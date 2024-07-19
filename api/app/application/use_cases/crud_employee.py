from math import ceil
from typing import Optional

from app.application.dto.all import PaginateDTO, PaginatedResults
from app.domain.entities.employee import Employee
from app.domain.repositories import EmployeeRepository


class CRUDEmployee:

    def __init__(self,
                 employee_repository: EmployeeRepository):
        self.__employee_repository = employee_repository

    def get_by_id(self, employee_id: str) -> Optional[Employee]:
        result = self.__employee_repository.get_by_id(employee_id)
        return result

    def all_employees(self, paginate: PaginateDTO) -> PaginatedResults:
        _all, total = self.__employee_repository.get_all(paginate.limit, offset=(paginate.page - 1) * paginate.limit)
        return PaginatedResults(
            page=paginate.page,
            total_pages=ceil(total / paginate.limit),
            total=total,
            results=_all
        )
