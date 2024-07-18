from typing import Optional, List

from app.domain.entities.product import Product
from app.domain.repositories import ProductRepository
from app.infrastructure.spark_session_builder import SparkSessionBuilder, SparkSessionSQLBuilder


class SparkProductRepository(ProductRepository):

    def filter(self, **kwargs) -> Optional[List[Product]]:
        pass

    def get_all(self) -> Optional[List[Product]]:
        pass

    def create(self, _new: Product) -> Optional[str]:
        raise NotImplementedError()

    def non_query(self, **kwargs) -> Optional[List[Product]]:
        pass

    def get_by_id(self, _id: str) -> Optional[Product]:
        with SparkSessionBuilder() as session:
            with SparkSessionSQLBuilder(session) as reader:
                reader.execute("SELECT 1")
                return None
