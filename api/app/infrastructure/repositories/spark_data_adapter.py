from typing import List

from app.domain.entities.employee import Employee, Sale


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
