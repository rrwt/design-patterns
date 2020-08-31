from abc import ABCMeta, abstractmethod


class StrategyInterface(metaclass=ABCMeta):
    """
    Interface common to all strategies.
    """

    @abstractmethod
    def execute(self):
        pass


class ConcreteStrategy1(StrategyInterface):
    """
    Concrete implementation of Strategy interface.
    Implements a variations of an algorithm the context uses.
    """

    def execute(self):
        print(f"{self.__class__.__name__}: Doing Something")


class ConcreteStrategy2(StrategyInterface):
    def execute(self):
        print(f"{self.__class__.__name__}: Doing Something else")


class Context:
    """
    This is the class we are trying to subdivide into several strategies.
    Maintains a reference to one of the concrete strategies and
    communicates with this object only via the strategy interface.
    It delegates the work to a linked strategy object instead of executing it on its own.
    """

    def __init__(self, strategy: StrategyInterface) -> None:
        self._strategy = strategy

    def do_something(self) -> None:
        """
        The context calls the execution method on the linked strategy
        object each time it needs to run the algorithm. The context
        doesn't know what type of strategy it works with or how the
        algorithm is executed
        """
        self._strategy.execute()


if __name__ == "__main__":
    strategy_1 = ConcreteStrategy1()
    strategy_2 = ConcreteStrategy2()

    for _ in (strategy_1, strategy_2):
        context = Context(_)
        context.do_something()
