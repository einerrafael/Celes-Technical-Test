from app.application.dto.all import PaginatedResults
from app.application.dto.employees import SalesEmployeeFilterDTO
from app.domain.entities.employee import Employee
from app.domain.repositories import EmployeeRepository


class SalesEmployee:

    def __init__(self,
                 employee_repository: EmployeeRepository):
        self.__employee_repository = employee_repository

    def total_sales_employee(self, dto: SalesEmployeeFilterDTO) -> PaginatedResults[Employee]:
        prod = self.__employee_repository.get_by_id(dto.employee_id)
        return PaginatedResults(
            page=1,
            total_pages=2,
            count=2,
            results=[]
        )
