from app.domain.repositories import EmployeeRepository, ProductRepository, StoreRepository
from app.infrastructure.repositories.spark_employee_repository import SparkEmployeeRepository
from app.infrastructure.repositories.spark_product_repository import SparkProductRepository
from app.infrastructure.repositories.spark_store_repository import SparkStoreRepository


class RepositoryFactory:

    @staticmethod
    def get_employee_repository() -> EmployeeRepository:
        return SparkEmployeeRepository()

    @staticmethod
    def get_product_repository() -> ProductRepository:
        return SparkProductRepository()

    @staticmethod
    def get_store_repository() -> StoreRepository:
        return SparkStoreRepository()
