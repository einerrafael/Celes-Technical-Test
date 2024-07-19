from builtins import any
from datetime import datetime
from typing import Optional

from app.domain.entities.employee import Employee
from app.domain.repositories import EmployeeRepository
from app.infrastructure.api.statuses import ResultsNotFound
from app.infrastructure.commons.date_utils import DateUtils
from app.infrastructure.repositories.spark_data_adapter import SparkDataAdapter
from app.infrastructure.spark_session_builder import SparkSessionBuilder, SparkSessionSQLBuilder


class SparkEmployeeRepository(EmployeeRepository):

    def total_sales_avg(self):
        view_name = "TotalSalesAvgEmployee"

        with SparkSessionBuilder() as session:
            with SparkSessionSQLBuilder(session, view_name) as reader:
                results = reader.execute(f"SELECT KeyEmployee as key, "
                                         f"COUNT(KeyEmployee) as count, "
                                         f"AVG(Amount) as avg, "
                                         f"SUM(Amount) as total"
                                         f" FROM {view_name} GROUP BY KeyEmployee ORDER BY 2 desc")
                results = results.collect()
                if not any(results):
                    raise ResultsNotFound()
                return SparkDataAdapter.parse_rows_to_statistic(results)

    def sales_by_employee_date_ranges(self,
                                      employee_id: str,
                                      start_date: datetime,
                                      end_date: datetime,
                                      limit: int,
                                      offset: int):
        view_name = "SalesEmployeeDateRanges"

        where_sentence = " WHERE KeyEmployee = {employee_id} "

        if start_date and end_date:
            where_sentence += " AND KeyDate between {start_date} and {end_date} "
        elif start_date:
            where_sentence += " AND KeyDate >= {start_date}"
        elif end_date:
            where_sentence += " AND KeyDate <= {end_date}"

        pagination_sentence = " LIMIT {limit} OFFSET {offset}"

        query = "SELECT * FROM " + view_name + where_sentence + pagination_sentence
        query_count = "SELECT count(*) as total FROM " + view_name + where_sentence

        args = {
            'employee_id': employee_id,
            'start_date': DateUtils.format_date(start_date, "%Y-%m-%d"),
            'end_date': DateUtils.format_date(end_date, "%Y-%m-%d"),
            'limit': limit,
            'offset': offset
        }

        with SparkSessionBuilder() as session:
            with SparkSessionSQLBuilder(session, view_name) as reader:
                results_query = reader.execute(query, args)
                results = results_query.collect()

                total_query = reader.execute(query_count, args)
                total = total_query.collect()[0]['total']

                return SparkDataAdapter.parse_rows_to_sales(results), total

    def get_all(self, limit: int = None, offset: int = None):
        sql = f"SELECT DISTINCT Employees FROM AllEmployees "
        sql_total = "SELECT COUNT(DISTINCT Employees) as total FROM AllEmployees"
        if limit:
            sql += f" limit {limit}"
        if offset:
            sql += f" offset {offset}"
        with SparkSessionBuilder() as session:
            with SparkSessionSQLBuilder(session, "AllEmployees") as reader:
                results_query = reader.execute(sql)
                results = results_query.collect()

                total_query = reader.execute(sql_total)
                total = total_query.collect()[0]['total']

                return SparkDataAdapter.parse_rows_to_employees(results), total

    def get_by_id(self, _id: str) -> Optional[Employee]:
        with SparkSessionBuilder() as session:
            with SparkSessionSQLBuilder(session, "EmployeeById") as reader:
                results = reader.execute("SELECT Employees FROM EmployeeById WHERE KeyEmployee = {id}", {'id': _id})
                results = results.collect()
                if not any(results):
                    return None
                return SparkDataAdapter.parse_row_to_employee(results[0])
