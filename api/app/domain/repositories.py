from abc import ABC, abstractmethod
from datetime import datetime

from app.domain.entities.employee import Employee
from app.domain.entities.product import Product
from app.domain.entities.store import Store
from app.infrastructure.repositories.base_repository import BaseRepository


class EmployeeRepository(BaseRepository[Employee, str], ABC):

    @abstractmethod
    def all_sales_by_employee(self, employee_id: str, limit: int, offset: int):
        pass

    @abstractmethod
    def sales_by_employee_date_ranges(self,
                                      employee_id: str,
                                      start_date: datetime,
                                      end_date: datetime,
                                      limit: int,
                                      offset: int, ):
        pass

    @abstractmethod
    def sales_total_by_employee(self, employee_id: str, limit: int, offset: int):
        pass


class StoreRepository(BaseRepository[Store, str], ABC):

    @abstractmethod
    def sales_by_store_date_ranges(self,
                                   _id: str,
                                   start_date: datetime,
                                   end_date: datetime,
                                   limit: int,
                                   offset: int, ):
        pass


class ProductRepository(BaseRepository[Product, str], ABC):

    @abstractmethod
    def sales_by_product_date_ranges(self,
                                     _id: str,
                                     start_date: datetime,
                                     end_date: datetime,
                                     limit: int,
                                     offset: int, ):
        pass
