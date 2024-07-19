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

    def __init__(self, session: SparkSession, view_name: str):
        self.__session = session
        self.__view_name = view_name

    @property
    def view_name(self):
        return self.__view_name

    def __enter__(self):
        with SparkParquetSQLReader(self.__session, self.PARQUET_FILES, self.view_name) as reader:
            return reader

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
