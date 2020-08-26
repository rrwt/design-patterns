"""
Using a decorator
"""


def singleton_decorator(klass):
    """
    A generic class decorator. can turn any class into a singleton
    by controlling its creation
    """
    __instances = {}

    def wrapper(*args, **kwargs):
        nonlocal __instances

        if __instances.get(klass) is None:
            __instances[klass] = klass(*args, **kwargs)

        return __instances[klass]

    return wrapper


@singleton_decorator
class Singleton:
    """
    This class will function as a singleton as long as
    it is being decorated by singleton_decorator
    """

    __instance = None

    def __init__(self) -> None:
        self.count = 0


if __name__ == "__main__":
    singleton_1 = Singleton()
    singleton_2 = Singleton()

    assert singleton_1 is singleton_2, "The `Singleton class` is not a singleton"

    assert singleton_1.count == 0
    singleton_2.count = 10
    assert singleton_1.count == 10
