"""
Furniture Shop.
We have all things Modern and Virtual
"""
from abc import abstractmethod, ABCMeta


class Chair(metaclass=ABCMeta):
    """
    Abstract Chair defining common methods all chairs must have
    """

    @abstractmethod
    def can_sit_on(self) -> bool:
        pass

    @abstractmethod
    def num_legs(self) -> int:
        pass


class ModernChair(Chair):
    def can_sit_on(self) -> bool:
        return True

    def num_legs(self) -> int:
        return 4


class VirtualChair(Chair):
    def can_sit_on(self) -> bool:
        return False

    def num_legs(self) -> int:
        return 1


class Table(metaclass=ABCMeta):
    """
    Abstract table defining common methods all tables must have
    """

    @abstractmethod
    def has_bbq_in_center(self) -> bool:
        pass


class ModernTable(Table):
    def has_bbq_in_center(self) -> bool:
        return False


class VirtualTable(Table):
    def has_bbq_in_center(self) -> bool:
        return True


class AbstractFurniture(metaclass=ABCMeta):
    """
    Interface declaring a set of methods for creating each of the abstract furniture
    """

    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def create_chair(self):
        pass


class ModernFurniture(AbstractFurniture):
    def create_table(self):
        return ModernTable()

    def create_chair(self):
        return ModernChair()


class VirtualFurniture(AbstractFurniture):
    def create_table(self):
        return VirtualTable()

    def create_chair(self):
        return VirtualChair()


if __name__ == "__main__":
    modern_furniture = ModernFurniture()
    chair = modern_furniture.create_chair()
    table = modern_furniture.create_table()
    print(chair.can_sit_on())
    print(table.has_bbq_in_center())
