import os
from pyspark.sql import SparkSession


class SparkSessionMixin:

    def __init__(self, session: SparkSession):
        self.__session = session

    @property
    def session(self) -> SparkSession:
        return self.__session


class SparkSessionProvider(SparkSessionMixin):
    APP_NAME = os.environ.get('SPARK_APP_NAME', 'CelesApp')

    def __init__(self):
        self.__session = SparkSession.builder \
            .appName(self.APP_NAME) \
            .getOrCreate()
        super().__init__(self.__session)

    def close(self):
        self.__session.stop()


class SparkParquetReader(SparkSessionMixin):

    def __init__(self, session: SparkSession, dir_files: str):
        super().__init__(session)
        self.session.read.parquet(dir_files)


class SQLSparkReader(SparkSessionMixin):

    def __init__(self, session: SparkSession):
        super().__init__(session)

    def execute(self, sql: str, args):
        return self.session.sql(sql, args)
