from datetime import datetime
from typing import Union

from fastapi import APIRouter

from app.application.dto.all import PaginateDTO
from app.application.dto.employees import SalesEmployeeFilterDTO
from app.application.use_cases.sales_employee import SalesEmployee
from app.infrastructure.repositories.spark_employee_repository import SparkEmployeeRepository

route_employee = APIRouter()


@route_employee.get("/{employee_id}/sales")
def employee_sales(employee_id: str,
                   page: int = 1,
                   limit: int = 10,
                   start_date: Union[datetime, None] = None,
                   end_date: Union[datetime, None] = None,):

    try:
        # Check the data
        input_dto = SalesEmployeeFilterDTO(
            employee_id=employee_id,
            start_date=start_date,
            end_date=end_date,
            pagination=PaginateDTO(
                page=page,
                limit=limit
            )
        )

        # Invoke the business logic
        sales_employee = SalesEmployee(
            employee_repository=SparkEmployeeRepository()
        )

        return sales_employee.total_sales_employee(input_dto)
    except Exception as ex:
        return 0
