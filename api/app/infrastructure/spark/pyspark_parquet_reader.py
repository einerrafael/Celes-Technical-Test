from pyspark.sql import SparkSession

from app.infrastructure.spark.pyspark_reader import SQLSparkReader, SparkParquetReader


class SparkParquetSQLReader:

    def __init__(self, session: SparkSession, dir_files: str):
        self.__parquet_reader = SparkParquetReader(session, dir_files)

    def __enter__(self) -> SQLSparkReader:
        return SQLSparkReader(self.__parquet_reader.session)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
