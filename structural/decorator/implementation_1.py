"""
Implement using Abstract Classes (Interface)
"""
import time
from abc import ABCMeta, abstractmethod


class ComponentInterface(metaclass=ABCMeta):
    """
    Defines a common interface for decorators and concrete components.
    """

    @abstractmethod
    def execute(self):
        pass


class ConcreteComponent(ComponentInterface):
    """
    ComponentInterface's concrete implementation.
    There can be more of these.
    """

    def execute(self):
        time.sleep(1)
        print(f"{self.__class__.__name__} was called")


class BaseDecorator(ComponentInterface, metaclass=ABCMeta):
    """
    An abstract class common to all decorators.
    It inherits from ComponentInterface to make sure
    that all decorators and concrete components have
    similar structure.
    """

    def __init__(self, wrapee) -> None:
        self._wrapee = wrapee

    @abstractmethod
    def execute(self):
        pass


class LoggingDecorator(BaseDecorator):
    """
    A class decorator to log information before and after execution.
    """

    def execute(self):
        print(f"{self.__class__.__name__}: Calling wrapee now.")
        self._wrapee.execute()
        print(f"{self.__class__.__name__}: wrapee was called.")


class TimeItDecorator(BaseDecorator):
    """
    A class decorator to note the time taken to execute wrapee
    """

    def execute(self):
        start_time = time.time()
        print(f"{self.__class__.__name__}: Calling wrapee now.")
        self._wrapee.execute()
        end_time = time.time()
        print(f"Total time of execution: {(end_time - start_time)} seconds")


if __name__ == "__main__":
    component = ConcreteComponent()
    logging_decorator = LoggingDecorator(component)
    time_it_decorator = TimeItDecorator(logging_decorator)
    time_it_decorator.execute()
