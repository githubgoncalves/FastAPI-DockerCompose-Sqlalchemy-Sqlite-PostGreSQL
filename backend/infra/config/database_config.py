import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from extensions.database_enum import DataBase

file_path = os.path.abspath(os.getcwd())+"\database.db"

class DbConnectionHandler():
    """Sqlalchemy database connection"""

    def __init__(self,database: str):
        print(F"DATABASE .ENV: {database}")
        if(database == DataBase.POSTGRESQL.name):
            print("ENTROU NO POSTGRESQL")
            self.__connection_string = "postgresql://postgres:123456@db:15432/postgres"
        if (database == DataBase.SQLITE.name):
            print("ENTROU NO SQLITE")
            self.__connection_string = 'sqlite:///'+file_path
        self.session = None

    def get_engine(self):
        """Return connection Engine
        :param - None
        :return - Engine connection database
        """
        engine = create_engine(self.__connection_string,echo=True)
        return engine

    def __enter__(self):
        engine = create_engine(self.__connection_string, echo = True)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()