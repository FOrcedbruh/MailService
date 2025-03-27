from abc import ABC, abstractmethod


class BaseBrokerClient(ABC):

    @classmethod
    @abstractmethod
    def get_consumer(cls): ...

