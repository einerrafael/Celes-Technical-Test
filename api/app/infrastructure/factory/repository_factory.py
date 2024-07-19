from app.domain.repositories import EmployeeRepository, ProductRepository
from app.infrastructure.repositories.spark_employee_repository import SparkEmployeeRepository
from app.infrastructure.repositories.spark_product_repository import SparkProductRepository


class RepositoryFactory:

    @staticmethod
    def get_employee_repository() -> EmployeeRepository:
        return SparkEmployeeRepository()

    @staticmethod
    def get_product_repository() -> ProductRepository:
        return SparkProductRepository()
