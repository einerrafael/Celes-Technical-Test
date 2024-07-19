from unittest.mock import MagicMock

from pytest import fixture

from app.application.dto.all import PaginateDTO
from app.domain.entities.employee import Employee
from app.domain.entities.product import Product
from app.domain.entities.store import Store
from app.infrastructure.repositories.spark_employee_repository import SparkEmployeeRepository
from app.infrastructure.repositories.spark_product_repository import SparkProductRepository
from app.infrastructure.repositories.spark_store_repository import SparkStoreRepository


@fixture
def employee_repository(mocker):
    mock_repository = MagicMock()
    mocker.patch.object(SparkEmployeeRepository, '__new__', return_value=mock_repository)
    return mock_repository


@fixture
def store_repository(mocker):
    mock_repository = MagicMock()
    mocker.patch.object(SparkStoreRepository, '__new__', return_value=mock_repository)
    return mock_repository


@fixture
def product_repository(mocker):
    mock_repository = MagicMock()
    mocker.patch.object(SparkProductRepository, '__new__', return_value=mock_repository)
    return mock_repository


# Mock Data
@fixture
def employee_1():
    return Employee(**{
            "key": "1|18335",
            "code": "18335",
            "division": "1",
            "name": "FERNANDEZ QUINTERO JUSEEN CAMILO",
            "position": None
        })


@fixture
def product_1():
    return Product(**{
            "key": "1|59836",
            "code": "7663",
            "sub_category_name": "PLANTAS MEDICINALES                     ",
            "category_name": None,
            "brand_name": "DROGUERIAS JULIAO",
            "name": "JB SEN HOJAS 50 GR"
        })


@fixture
def store_1():
    return Store(**{
            "key": "1|021",
            "code": "021",
            "name": "CALLE93",
            "country": None,
            "city": None,
            "province": None,
            "type": "CENTRO OPERATIVO"
        })


@fixture
def paginate_dto():
    return PaginateDTO(
        page=1,
        limit=10,
    )
