from datetime import datetime
from typing import Optional, List

from app.domain.entities.product import Product
from app.domain.repositories import ProductRepository
from app.infrastructure.api.statuses import ResultsNotFound
from app.infrastructure.commons.date_utils import DateUtils
from app.infrastructure.repositories.spark_data_adapter import SparkDataAdapter
from app.infrastructure.spark_session_builder import SparkSessionBuilder, SparkSessionSQLBuilder


class SparkProductRepository(ProductRepository):

    def total_sales_avg(self):
        view_name = "TotalSalesAvgProduct"

        with SparkSessionBuilder() as session:
            with SparkSessionSQLBuilder(session, view_name) as reader:
                results = reader.execute(f"SELECT KeyProduct as key, "
                                         f"COUNT(KeyProduct) as count, "
                                         f"AVG(Amount) as avg, "
                                         f"SUM(Amount) as total"
                                         f" FROM {view_name} GROUP BY KeyProduct ORDER BY 2 desc")
                results = results.collect()
                if not any(results):
                    raise ResultsNotFound()
                return SparkDataAdapter.parse_rows_to_statistic(results)

    def sales_by_product_date_ranges(self,
                                     _id: str,
                                     start_date: datetime,
                                     end_date: datetime,
                                     limit: int,
                                     offset: int):
        view_name = "SalesProductDateRanges"

        where_sentence = " WHERE KeyProduct = {_id} "

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
            '_id': _id,
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
        sql = f"SELECT DISTINCT Products FROM AllProducts "
        sql_total = "SELECT COUNT(DISTINCT Products) as total FROM AllProducts"
        if limit:
            sql += f" limit {limit}"
        if offset:
            sql += f" offset {offset}"
        with SparkSessionBuilder() as session:
            with SparkSessionSQLBuilder(session, "AllProducts") as reader:
                results_query = reader.execute(sql)
                results = results_query.collect()

                total_query = reader.execute(sql_total)
                total = total_query.collect()[0]['total']

                return SparkDataAdapter.parse_rows_to_products(results), total

    def get_by_id(self, _id: str) -> Optional[Product]:
        with SparkSessionBuilder() as session:
            with SparkSessionSQLBuilder(session, "ProductById") as reader:
                results = reader.execute("SELECT Products FROM EmployeeById WHERE KeyProduct = {id}", {'id': _id})
                results = results.collect()
                if not any(results):
                    raise ResultsNotFound()
                return SparkDataAdapter.parse_row_to_product(results[0])
