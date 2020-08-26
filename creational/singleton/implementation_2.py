"""
Using a metaclass
"""


class MetaSingleton(type):
    """
    A generic singleton metaclass.
    Can be used with any class desiring to be a singleton
    """

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class Singleton(metaclass=MetaSingleton):
    """
    Using a metaclass to hide details from clients of current class.
    """

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)

        return cls.__instance


if __name__ == "__main__":
    singleton_1 = Singleton()
    singleton_2 = Singleton()

    assert singleton_1 is singleton_2, "The `Singleton class` is not a singleton"

    singleton_3 = Singleton.__new__(Singleton)
    assert singleton_1 is singleton_3, "The `Singleton class` is not a singleton"
