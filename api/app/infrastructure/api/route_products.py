import logging
from datetime import datetime
from typing import Union

from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

from app.application.dto.all import PaginateDTO, ResponseMessage, ResponseMessageCode, ResponseStatus
from app.application.dto.employees import SalesProductFilterDTO
from app.application.uses_cases.crud_product import CRUDProduct
from app.application.uses_cases.sales_information import SalesInformation
from app.infrastructure.api.statuses import ResultsNotFound
from app.infrastructure.factory.repository_factory import RepositoryFactory

route_product = APIRouter()

logger = logging.getLogger(__name__)


@route_product.get("/")
def all_products(page: int = 1,
                 limit: int = 10, ):
    try:
        pagination = PaginateDTO(
            page=page,
            limit=limit
        )
        crud = CRUDProduct(
            product_repository=RepositoryFactory.get_product_repository()
        )

        return crud.all_products(pagination)
    except ResultsNotFound as nf:
        return ResponseMessage(
            code=ResponseMessageCode.EMPTY_RESULTS,
            status=ResponseStatus.INFO,
            message=""
        )

    except Exception as ex:
        logger.exception(ex)
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="error")


@route_product.get("/{_id}")
def get_product_by_id(_id: str, ):
    try:
        crud = CRUDProduct(
            product_repository=RepositoryFactory.get_product_repository()
        )

        return crud.get_by_id(_id)
    except ResultsNotFound:
        return ResponseMessage(
            code=ResponseMessageCode.EMPTY_RESULTS,
            status=ResponseStatus.INFO,
            message=""
        )

    except Exception as ex:
        logger.exception(ex)
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="error")


@route_product.get("/{_id}/sales")
def employee_sales(_id: str,
                   page: int = 1,
                   limit: int = 10,
                   start_date: Union[datetime, None] = None,
                   end_date: Union[datetime, None] = None, ):
    try:
        # Check the data
        input_dto = SalesProductFilterDTO(
            product_id=_id,
            start_date=start_date,
            end_date=end_date,
            pagination=PaginateDTO(
                page=page,
                limit=limit
            )
        )

        # Invoke the business logic
        sales_information = SalesInformation(
            employee_repository=RepositoryFactory.get_employee_repository(),
            product_repository=RepositoryFactory.get_product_repository(),
            store_repository=RepositoryFactory.get_store_repository(),
        )

        return sales_information.all_sales_product(input_dto)
    except ResultsNotFound as nf:
        return ResponseMessage(
            code=ResponseMessageCode.EMPTY_RESULTS,
            status=ResponseStatus.INFO,
            message=""
        )

    except Exception as ex:
        logger.exception(ex)
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="error")


@route_product.get("/all/statistics")
def statistics_products():
    try:
        sales_info = SalesInformation(
            employee_repository=RepositoryFactory.get_employee_repository(),
            product_repository=RepositoryFactory.get_product_repository(),
            store_repository=RepositoryFactory.get_store_repository(),
        )

        return sales_info.statistics_product()
    except ResultsNotFound as nf:
        return ResponseMessage(
            code=ResponseMessageCode.EMPTY_RESULTS,
            status=ResponseStatus.INFO,
            message=""
        )

    except Exception as ex:
        logger.exception(ex)
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="error")
