from abc import ABC, abstractmethod

class DataSource(ABC):
    @abstractmethod
    def read_data(self):
        pass

class FileDataSource(DataSource):
    def __init__(self, file_name: str):
        self.file_name = file_name

    def read_data(self):
        return 'Содержимое файла'

class DatabaseDataSource:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def fetch_data(self):
        return 'Содержимое базы данных'

class DatabaseAdapter(DataSource):
    def __init__(self, db_src: DatabaseDataSource):
        self.db_src = db_src 

    def read_data(self):
        return self.db_src.fetch_data()
