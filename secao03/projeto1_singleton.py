import sqlite3
from typing import Any, Dict


class Singleton(type):

    __instances: Dict[type, type] = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(
                *args,
                **kwargs
            )
        return cls.__instances[cls]


class Database(metaclass=Singleton):

    connection = None

    @classmethod
    def connect(cls):
        if cls.connection is None:
            print(f'Não temos ainda uma conexão, vamor criá-la.')
            cls.connection = sqlite3.connect('secao03/db.geek')
            cls.cursor = cls.connection.cursor()
        return cls.cursor


db1 = Database().connect()

db2 = Database().connect()
