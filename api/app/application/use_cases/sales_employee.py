from math import ceil

from app.application.dto.all import PaginatedResults
from app.application.dto.employees import SalesEmployeeFilterDTO
from app.domain.entities.employee import Employee
from app.domain.repositories import EmployeeRepository


class SalesEmployee:

    def __init__(self,
                 employee_repository: EmployeeRepository):
        self.__employee_repository = employee_repository

    def total_sales_employee(self, dto: SalesEmployeeFilterDTO) -> PaginatedResults:
        results, total = (self.__employee_repository.
                          sales_by_employee_date_ranges(dto.employee_id,
                                                        dto.start_date,
                                                        dto.end_date,
                                                        dto.pagination.limit,
                                                        offset=(dto.pagination.page - 1) * dto.pagination.limit
                                                        ))
        return PaginatedResults(
            page=dto.pagination.page,
            total_pages=ceil(total / dto.pagination.limit),
            total=total,
            results=results
        )
