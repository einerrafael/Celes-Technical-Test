import logging
from datetime import datetime
from typing import Union

from fastapi import APIRouter, HTTPException, Depends
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

from app.application.dto.all import PaginateDTO, ResponseMessage, ResponseMessageCode, ResponseStatus
from app.application.dto.employees import SalesEmployeeFilterDTO
from app.application.uses_cases.crud_employee import CRUDEmployee
from app.application.uses_cases.sales_information import SalesInformation
from app.infrastructure.api.statuses import ResultsNotFound
from app.infrastructure.auth.auth_manager import verify_token
from app.infrastructure.factory.repository_factory import RepositoryFactory

route_employee = APIRouter(dependencies=[Depends(verify_token)])

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
            employee_repository=RepositoryFactory.get_employee_repository(),
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
            employee_repository=RepositoryFactory.get_employee_repository(),
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
            employee_repository=RepositoryFactory.get_employee_repository(),
            product_repository=RepositoryFactory.get_product_repository(),
            store_repository=RepositoryFactory.get_store_repository(),
        )

        return sales_employee.all_sales_employee(input_dto)
    except ResultsNotFound as nf:
        return ResponseMessage(
            code=ResponseMessageCode.EMPTY_RESULTS,
            status=ResponseStatus.INFO,
            message=""
        )

    except Exception as ex:
        logger.exception(ex)
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="error")


@route_employee.get("/all/statistics")
def statistics_employees():
    try:
        sales_info = SalesInformation(
            employee_repository=RepositoryFactory.get_employee_repository(),
            product_repository=RepositoryFactory.get_product_repository(),
            store_repository=RepositoryFactory.get_store_repository(),
        )

        return sales_info.statistics_employee()
    except ResultsNotFound as nf:
        return ResponseMessage(
            code=ResponseMessageCode.EMPTY_RESULTS,
            status=ResponseStatus.INFO,
            message=""
        )

    except Exception as ex:
        logger.exception(ex)
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="error")
