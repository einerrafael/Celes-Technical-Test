from pyspark.sql import SparkSession

from app.infrastructure.spark.pyspark_reader import SQLSparkReader, SparkParquetReader


class SparkParquetSQLReader:

    def __init__(self, session: SparkSession, dir_files: str, view_name: str):
        self.__view_name = view_name
        self.__parquet_reader = SparkParquetReader(session, dir_files)
        if view_name:
            self.__parquet_reader.df.createTempView(view_name)

    @property
    def view_name(self):
        return self.__view_name

    def __enter__(self) -> SQLSparkReader:
        return SQLSparkReader(self.__parquet_reader.session)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
