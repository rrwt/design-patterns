from abc import abstractmethod, ABCMeta


class FactoryMethodInterface(metaclass=ABCMeta):
    """
    Interface common to all factory method classes.
    Also known as Product.
    """

    @abstractmethod
    def do_stuff(self):
        pass


class ConcreteProductA(FactoryMethodInterface):
    """
    One of the implementation of factory method's product
    """

    def do_stuff(self) -> None:
        print(f"{self.__class__.__name__}: Doing stuff")


class ConcreteProductB(FactoryMethodInterface):
    def do_stuff(self) -> None:
        print(f"{self.__class__.__name__}: Doing stuff")


class BaseCreator(metaclass=ABCMeta):
    """
    Declares the factory method that returns new Factory object.
    """

    def __init__(self) -> None:
        self.product = self._create_product()

    @abstractmethod
    def _create_product(self) -> FactoryMethodInterface:
        pass


class ConcreteCreatorA(BaseCreator):
    """
    Works with ConcreteProductA.
    """

    def _create_product(self) -> FactoryMethodInterface:
        return ConcreteProductA()


class ConcreteCreatorB(BaseCreator):
    """
    Works with ConcreteProductB.
    """

    def _create_product(self) -> FactoryMethodInterface:
        return ConcreteProductB()


if __name__ == "__main__":
    cca = ConcreteCreatorA()
    cca.product.do_stuff()
    ccb = ConcreteCreatorB()
    ccb.product.do_stuff()
