from abc import ABCMeta, abstractmethod


class Publisher:
    """
    Observable/Subject
    Subscribers subscribe to messages from this class.
    It maintains a list of subscribers and notifies them of an event.
    New subscribers can join and existing ones can leave when they want.
    Generally there is no particular order in which the subscribers
    should be notified.
    """

    def __init__(self) -> None:
        self.__subscribers = set()
        self._state = "Happy"

    def subscribe(self, subscriber) -> None:
        self.__subscribers.add(subscriber)

    def unsubscribe(self, subscriber) -> None:
        if subscriber in self.__subscribers:
            self.__subscribers.remove(subscriber)

    def notify_subscribers(self) -> None:
        for subscriber in self.__subscribers:
            subscriber.update(self._state)

    def do_stuff(self) -> None:
        print(f"{self.__class__.__name__}: Doing stuff")

    @property
    def state(self) -> str:
        return self._state

    @state.setter
    def state(self, value: str) -> None:
        self._state = value


class Subscriber(metaclass=ABCMeta):
    """
    Observer/Listener
    Common Interface for all subscribers. Implementing this interface
    will make sure that publisher can use a common update() to notify
    all subscribers.
    """

    @abstractmethod
    def update(self, data):
        pass


class ConcreteSubscriber(Subscriber):
    """
    Concrete implementation of Subscriber interface
    """

    def update(self, data: str) -> None:
        print(f"{self.__class__.__name__} received following message: {data}")


if __name__ == "__main__":
    pub = Publisher()
    sub = ConcreteSubscriber()
    pub.subscribe(sub)

    pub.notify_subscribers()
    pub.state = "How you doin?"
    pub.notify_subscribers()
