from typing import List

from app.domain.entities.consolidated import StatisticTotAvg
from app.domain.entities.employee import Employee, Sale
from app.domain.entities.product import Product
from app.domain.entities.store import Store


class SparkDataAdapter:

    @staticmethod
    def parse_row_to_employee(row: list) -> Employee:
        return Employee(
            key=row[0].__getitem__('KeyEmployee'),
            code=row[0].__getitem__('EmployeeCode'),
            division=row[0].__getitem__('KeyDivision'),
            name=row[0].__getitem__('EmployeeName'),
            position=row[0].__getitem__('JobPosition'),
        )

    @classmethod
    def parse_rows_to_employees(cls, rows: list) -> List[Employee]:
        return [cls.parse_row_to_employee(row) for row in rows]

    @staticmethod
    def parse_row_to_product(row) -> Product:
        return Product(
            key=row[0].__getitem__('KeyProduct'),
            code=row[0].__getitem__('ProductCode'),
            sub_category_name=row[0].__getitem__('SubCategoryName'),
            category_name=row[0].__getitem__('CategoryName'),
            brand_name=row[0].__getitem__('BrandName'),
            name=row[0].__getitem__('ProductName'),
        )

    @classmethod
    def parse_rows_to_products(cls, rows: list) -> List[Product]:
        return [cls.parse_row_to_product(row) for row in rows]

    @staticmethod
    def parse_row_to_sale(row) -> Sale:
        return Sale(
            key=row.__getitem__('KeySale'),
            date=row.__getitem__('KeyDate'),
            store_key=row.__getitem__('KeyStore'),
            customer_key=row.__getitem__('KeyCustomer'),
            product_key=row.__getitem__('KeyProduct'),
            amount=row.__getitem__('Amount'),
            ticket_key=row.__getitem__('KeyTicket'),
        )

    @classmethod
    def parse_rows_to_sales(cls, rows: list) -> List[Sale]:
        return [cls.parse_row_to_sale(row) for row in rows]

    @staticmethod
    def parse_row_to_store(row) -> Store:
        return Store(
            key=row[0].__getitem__('KeyStore'),
            code=row[0].__getitem__('StoreCode'),
            name=row[0].__getitem__('StoreName'),
            country=row[0].__getitem__('Country'),
            city=row[0].__getitem__('City'),
            province=row[0].__getitem__('Province'),
            type=row[0].__getitem__('StoreType'),
        )

    @classmethod
    def parse_rows_to_stores(cls, rows: list) -> List[Store]:
        return [cls.parse_row_to_store(row) for row in rows]

    @staticmethod
    def parse_row_to_statistic(row) -> StatisticTotAvg:
        return StatisticTotAvg(
            key=row.__getitem__('key'),
            count=row.__getitem__('count'),
            avg=row.__getitem__('avg'),
            total=row.__getitem__('total'),
        )

    @classmethod
    def parse_rows_to_statistic(cls, rows: list) -> List[StatisticTotAvg]:
        return [cls.parse_row_to_statistic(row) for row in rows]
