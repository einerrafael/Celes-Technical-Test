from datetime import datetime
from typing import Optional, List

from app.domain.entities.employee import Employee
from app.domain.repositories import EmployeeRepository
from app.infrastructure.spark_session_builder import SparkSessionBuilder, SparkSessionSQLBuilder


class SparkEmployeeRepository(EmployeeRepository):

    def all_sales_by_employee(self, employee_id: str, limit: int, offset: int):
        pass

    def sales_total_by_employee(self, employee_id: str, limit: int, offset: int):
        pass

    def sales_by_employee_date_ranges(self, employee_id: str, start_date: datetime, end_date: datetime, limit: int,
                                      offset: int):
        pass

    def get_all(self, limit: int = None) -> Optional[List[Employee]]:
        with SparkSessionBuilder() as session:
            with SparkSessionSQLBuilder(session, "AllEmployees") as reader:
                results = reader.execute(f"SELECT Employees FROM AllEmployees" + f" limit {limit}" if limit else '')
                print(results.collect())
                return None

    def get_by_id(self, _id: str) -> Optional[Employee]:
        with SparkSessionBuilder() as session:
            with SparkSessionSQLBuilder(session, "EmployeeById") as reader:
                results = reader.execute("SELECT Employees FROM EmployeeById WHERE KeyEmployee = {id}", {'id': _id})
                results = results.collect()
                return results
