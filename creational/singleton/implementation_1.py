"""
By controlling access to __init__
"""


class Singleton:
    """
    It is not possible to initialize this class directly.
    Use get_instance() method to get an instance of the class to work with
    """

    __instance = None

    def __init__(self) -> None:
        self._count = 0
        raise RuntimeError(
            f"Please call get_instance() class method"
            f" to get an instance of {self.__class__.__name__}"
        )

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)

        return cls.__instance

    @classmethod
    def get_instance(cls) -> "Singleton":
        return Singleton.__new__(cls)


if __name__ == "__main__":
    try:
        Singleton()
    except RuntimeError as e:
        print(e)

    singleton_1 = Singleton.get_instance()
    singleton_2 = Singleton.get_instance()

    assert singleton_1 is singleton_2, "The `Singleton class` is not a singleton"

    singleton_3 = Singleton.__new__(Singleton)
    assert singleton_1 is singleton_3, "The `Singleton class` is not a singleton"
