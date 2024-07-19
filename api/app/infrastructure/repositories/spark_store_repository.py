from datetime import datetime
from typing import Optional

from app.domain.entities.store import Store
from app.domain.repositories import StoreRepository
from app.infrastructure.api.statuses import ResultsNotFound
from app.infrastructure.commons.date_utils import DateUtils
from app.infrastructure.repositories.spark_data_adapter import SparkDataAdapter
from app.infrastructure.spark_session_builder import SparkSessionBuilder, SparkSessionSQLBuilder


class SparkStoreRepository(StoreRepository):

    def total_sales_avg(self):
        view_name = "TotalSalesAvgStore"

        with SparkSessionBuilder() as session:
            with SparkSessionSQLBuilder(session, view_name) as reader:
                results = reader.execute(f"SELECT KeyStore as key, "
                                         f"COUNT(KeyStore) as count, "
                                         f"AVG(Amount) as avg, "
                                         f"SUM(Amount) as total"
                                         f" FROM {view_name} GROUP BY KeyStore ORDER BY 2 desc")
                results = results.collect()
                if not any(results):
                    raise ResultsNotFound()
                return SparkDataAdapter.parse_rows_to_statistic(results)

    def sales_by_store_date_ranges(self,
                                   _id: str,
                                   start_date: datetime,
                                   end_date: datetime,
                                   limit: int,
                                   offset: int):
        view_name = "SalesStoreDateRanges"

        where_sentence = " WHERE KeyStore = {_id} "

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
        sql = f"SELECT DISTINCT Stores FROM AllStores "
        sql_total = "SELECT COUNT(DISTINCT Stores) as total FROM AllStores"
        if limit:
            sql += f" limit {limit}"
        if offset:
            sql += f" offset {offset}"
        with SparkSessionBuilder() as session:
            with SparkSessionSQLBuilder(session, "AllStores") as reader:
                results_query = reader.execute(sql)
                results = results_query.collect()

                total_query = reader.execute(sql_total)
                total = total_query.collect()[0]['total']

                return SparkDataAdapter.parse_rows_to_stores(results), total

    def get_by_id(self, _id: str) -> Optional[Store]:
        with SparkSessionBuilder() as session:
            with SparkSessionSQLBuilder(session, "StoreById") as reader:
                results = reader.execute("SELECT Stores FROM StoreById WHERE KeyStore = {id}", {'id': _id})
                results = results.collect()
                if not any(results):
                    raise ResultsNotFound()
                return SparkDataAdapter.parse_row_to_store(results[0])
