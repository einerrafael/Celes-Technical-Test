from math import ceil

from app.application.dto.all import PaginatedResults
from app.application.dto.employees import SalesEmployeeFilterDTO, SalesProductFilterDTO
from app.domain.repositories import EmployeeRepository, ProductRepository


class SalesInformation:

    def __init__(self,
                 employee_repository: EmployeeRepository,
                 product_repository: ProductRepository):
        self.__employee_repository = employee_repository
        self.__product_repository = product_repository

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

    def total_sales_product(self, dto: SalesProductFilterDTO) -> PaginatedResults:
        results, total = (self.__product_repository.
                          sales_by_product_date_ranges(dto.product_id,
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
