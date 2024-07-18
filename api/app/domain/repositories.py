from abc import ABC

from app.domain.entities.employee import Employee
from app.domain.entities.product import Product
from app.domain.entities.store import Store
from app.infrastructure.repositories.base_repository import BaseRepository


class EmployeeRepository(BaseRepository[Employee, str], ABC):
    pass


class StoreRepository(BaseRepository[Store, str], ABC):
    pass


class ProductRepository(BaseRepository[Product, str], ABC):
    pass
