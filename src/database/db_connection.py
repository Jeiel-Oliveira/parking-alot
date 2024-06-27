from abc import ABC, abstractmethod


class DbConnection(ABC):
    @abstractmethod
    def connect():
        pass

    @abstractmethod
    def disconnect():
        pass
