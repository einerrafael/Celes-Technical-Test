from unittest.mock import MagicMock

from pytest import fixture

from app.application.dto.all import PaginateDTO
from app.domain.entities.employee import Employee
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
    return Employee(
        key="1|22",
        code="Some",
        division="Height",
        name="Pepito Perez",
        position=None
    )


@fixture
def paginate_dto():
    return PaginateDTO(
        page=1,
        limit=10,
    )
