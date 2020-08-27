from random import random
from typing import Optional


class BaseHandler:
    """
    Abstract class defining common behaviors for all concrete handlers
    """

    def __init__(self, next_handler: Optional["BaseHandler"] = None) -> None:
        """
        Set the next handler in the chain
        """
        self._next_handler = next_handler

    def handle(self, request: float) -> None:
        """
        Common handler. Passes the request to next handler if there is one
        """
        if self._next_handler is not None:
            self._next_handler.handle(request)
        else:
            print("The request cannot be handled")


class ConcreteHandler1(BaseHandler):
    """
    One of the implementations
    """

    def handle(self, request: float) -> None:
        if request > 0.6:
            print(f"Handled by {self.__class__.__name__}")
        else:
            super().handle(request)


class ConcreteHandler2(BaseHandler):
    def handle(self, request: float) -> None:
        if request < 0.4:
            print(f"Handled by {self.__class__.__name__}")
        else:
            super().handle(request)


if __name__ == "__main__":
    handler1 = ConcreteHandler1()
    handler2 = ConcreteHandler2(handler1)

    for _ in range(10):
        handler2.handle(random())
