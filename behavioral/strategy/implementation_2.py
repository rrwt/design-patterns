"""
Example application.
Do various arithmetic calculations.
"""

from abc import ABCMeta, abstractmethod


class Arithmetics(metaclass=ABCMeta):
    @abstractmethod
    def calculate(self, first: float, second: float) -> float:
        pass


class Add(Arithmetics):
    def calculate(self, first: float, second: float) -> float:
        return first + second


class Subtract(Arithmetics):
    def calculate(self, first: float, second: float) -> float:
        return first - second


class Multiply(Arithmetics):
    def calculate(self, first: float, second: float) -> float:
        return first * second


class Divide(Arithmetics):
    def calculate(self, first: float, second: float) -> float:
        try:
            return first / second
        except ZeroDivisionError:
            raise ZeroDivisionError("Divisor cannot be 0")


class Context:
    def __init__(self, strategy: Arithmetics) -> None:
        self._strategy = strategy

    def execute(self, first: float, second: float) -> float:
        return self._strategy.calculate(first, second)


if __name__ == "__main__":
    context = Context(Add())
    print(context.execute(10, 10))
