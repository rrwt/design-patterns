"""
Implementing a logistics module for road and sea logistics.
Can be extended for other modes of transportation.
"""


from abc import abstractmethod, ABCMeta


class Transport(metaclass=ABCMeta):
    """
    Transport interface common to all implementations
    """

    @abstractmethod
    def deliver(self):
        pass


class Truck(Transport):
    def deliver(self) -> None:
        print(f"{self.__class__.__name__}: Delivering by land in a box")


class Ship(Transport):
    def deliver(self) -> None:
        print(f"{self.__class__.__name__}: Delivering by sea in a container")


class Logistics(metaclass=ABCMeta):
    """
    Base common to all logistics
    """

    def __init__(self) -> None:
        self.transport = self._create_transport()

    def plan_delivery(self) -> None:
        self.transport.deliver()

    @abstractmethod
    def _create_transport(self) -> Transport:
        pass


class RoadLogistics(Logistics):
    """
    If a client wants to use road logistics to deliver goods
    """

    def _create_transport(self) -> Transport:
        return Truck()


class SeaLogistics(Logistics):
    """
    If a client wants to use seaway.
    """

    def _create_transport(self) -> Transport:
        return Ship()


if __name__ == "__main__":
    rl = RoadLogistics()
    sl = SeaLogistics()

    rl.plan_delivery()
    sl.plan_delivery()
