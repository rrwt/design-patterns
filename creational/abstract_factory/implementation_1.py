from abc import abstractmethod, ABCMeta


class AbstractProductA(metaclass=ABCMeta):
    """
    Declares interface for a set of distinct but related products
    which make up a product family.
    """

    @abstractmethod
    def do_something(self) -> None:
        pass


class ConcreteProductA1(AbstractProductA):
    """
    Implementation of abstract products grouped by variants.
    """

    def do_something(self) -> None:
        print(f"{self.__class__.__name__}: Doing something")


class ConcreteProductA2(AbstractProductA):
    def do_something(self) -> None:
        print(f"{self.__class__.__name__}: Doing something else")


class AbstractProductB(metaclass=ABCMeta):
    @abstractmethod
    def do_something(self) -> None:
        pass


class ConcreteProductB1(AbstractProductB):
    def do_something(self) -> None:
        print(f"{self.__class__.__name__}: Busy doing stuff")


class ConcreteProductB2(AbstractProductB):
    def do_something(self) -> None:
        print(f"{self.__class__.__name__}: Busy doing other stuff")


class AbstractFactory(metaclass=ABCMeta):
    """
    Interface declaring a set of methods for creating each of the abstract products
    """

    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass


class ConcreteFactory1(AbstractFactory):
    """
    Implements creation methods of AbstractFactory.
    Each ConcreteFactory corresponds to a specific variant
    of products and only creates those products
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


if __name__ == "__main__":
    p1 = ConcreteFactory1()
    p1c1 = p1.create_product_a()
    p1c2 = p1.create_product_b()

    p1c1.do_something()
    p1c2.do_something()

    p2 = ConcreteFactory2()
    p2c1 = p2.create_product_a()
    p2c2 = p2.create_product_b()

    p2c1.do_something()
    p2c2.do_something()
