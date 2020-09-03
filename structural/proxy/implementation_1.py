"""
DB caching
"""
from abc import ABCMeta, abstractmethod


class DBInterface(metaclass=ABCMeta):
    """
    declares the interface of the Service. The proxy must follow this
    interface to be able to disguise itself as a service object.
    """

    @abstractmethod
    def query(self, key: str) -> str:
        pass


class DBService(DBInterface):
    """
    A class providing useful business logic
    """

    def __init__(self):
        self.__database = {"key": "value", "ping": "pong"}

    def query(self, key: str) -> str:
        print(f"fetching data from db. Select {key} from expensive_table;")
        return self.__database[key]


class DBProxy(DBInterface):
    """
    The Proxy class has a reference field that points to a service object.
    After the proxy finishes its processing (e.g., lazy initialization,
    logging, access control, caching, etc.), it passes the request to the
    service object. Usually, proxies manage the full lifecycle of their
    service objects.
    """

    def __init__(self) -> None:
        self.__cache = {}
        self.__service = None

    def query(self, key: str) -> str:
        if not self.__service:
            self.__service = DBService()

        if key not in self.__cache:
            self.__cache[key] = self.__service.query(key)

        return self.__cache[key]


if __name__ == "__main__":
    db = DBProxy()
    print("querying for ping")
    print(db.query("ping"))
    print("querying for ping")
    print(db.query("ping"))
