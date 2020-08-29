"""
Object Adapter:
    This implementation uses the composition principle:
    the adapter implements the interface of one object
    and wraps the other one.
"""
from abc import ABCMeta, abstractmethod


class Service:
    """
    Some useful class. e.g. a third party library
    """

    def service_method(self, service_data: float) -> float:
        # Only accepts numeric values.
        return 2 * service_data


class ClientInterface(metaclass=ABCMeta):
    """
    Describes the protocol that other classes must follow to be
    able to collaborate with the client code
    """

    @abstractmethod
    def method(self, data) -> float:
        pass


class Adapter(ClientInterface):
    """
    Works with both the client and the service.
    Wraps the service and implements the client interface.
    """

    def __init__(self) -> None:
        self.__adaptee = Service()

    def _convert_to_service_format(self, data: str) -> float:
        return float(data)

    def method(self, data: str) -> float:
        # has to work with string numbers and floating point values
        service_data = self._convert_to_service_format(data)
        return self.__adaptee.service_method(service_data)


if __name__ == "__main__":
    adapter = Adapter()
    double_pi = adapter.method("3.14159")
    assert isinstance(double_pi, float)
    print(double_pi)
