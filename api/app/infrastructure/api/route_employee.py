import logging
from datetime import datetime
from typing import Union

from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

from app.application.dto.all import PaginateDTO, ResponseMessage, ResponseMessageCode, ResponseStatus
from app.application.dto.employees import SalesEmployeeFilterDTO
from app.application.use_cases.crud_employee import CRUDEmployee
from app.application.use_cases.sales_information import SalesInformation
from app.infrastructure.api.statuses import ResultsNotFound
from app.infrastructure.repositories.spark_employee_repository import SparkEmployeeRepository

route_employee = APIRouter()

logger = logging.getLogger(__name__)


@route_employee.get("/")
def all_employees(page: int = 1,
                  limit: int = 10, ):
    try:
        pagination = PaginateDTO(
            page=page,
            limit=limit
        )

        # Invoke the business logic
        crud_employee = CRUDEmployee(
            employee_repository=SparkEmployeeRepository()
        )

        return crud_employee.all_employees(pagination)
    except ResultsNotFound as nf:
        return ResponseMessage(
            code=ResponseMessageCode.EMPTY_RESULTS,
            status=ResponseStatus.INFO,
            message=""
        )

    except Exception as ex:
        logger.exception(ex)
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="error")


@route_employee.get("/{employee_id}")
def get_employee_by_id(employee_id: str, ):
    try:
        # Invoke the business logic
        crud_employee = CRUDEmployee(
            employee_repository=SparkEmployeeRepository()
        )

        return crud_employee.get_by_id(employee_id)
    except ResultsNotFound as nf:
        return ResponseMessage(
            code=ResponseMessageCode.EMPTY_RESULTS,
            status=ResponseStatus.INFO,
            message=""
        )

    except Exception as ex:
        logger.exception(ex)
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="error")


@route_employee.get("/{employee_id}/sales")
def employee_sales(employee_id: str,
                   page: int = 1,
                   limit: int = 10,
                   start_date: Union[datetime, None] = None,
                   end_date: Union[datetime, None] = None, ):
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
        sales_employee = SalesInformation(
            employee_repository=SparkEmployeeRepository()
        )

        return sales_employee.total_sales_employee(input_dto)
    except ResultsNotFound as nf:
        return ResponseMessage(
            code=ResponseMessageCode.EMPTY_RESULTS,
            status=ResponseStatus.INFO,
            message=""
        )

    except Exception as ex:
        logger.exception(ex)
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="error")
