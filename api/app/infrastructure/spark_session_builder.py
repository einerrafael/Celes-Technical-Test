import os

from pyspark.sql import SparkSession

from app.infrastructure.spark.pyspark_parquet_reader import SparkParquetSQLReader
from app.infrastructure.spark.pyspark_reader import SparkSessionProvider


class SparkSessionBuilder:

    def __enter__(self) -> SparkSession:
        self.provider = SparkSessionProvider()
        return self.provider.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.provider.close()


class SparkSessionSQLBuilder:

    PARQUET_FILES = os.getenv('PARQUET_FILES_FOLDER', './assets/data/parquets')

    def __init__(self, session: SparkSession):
        self.__session = session

    def __enter__(self):
        with SparkParquetSQLReader(self.__session, self.PARQUET_FILES) as reader:
            return reader

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
