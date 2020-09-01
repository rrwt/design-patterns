from typing import Optional


class SubSystemA:
    """
    One of the complex subsystem a client wants to use.
    This could be a 3rd party library, a legacy system or
    anything requiring complex set of calls to perform some action.
    """

    def execute_me(self) -> None:
        print(f"{self.__class__.__name__}: Executing")


class SubSystemB:
    def execute_me(self) -> None:
        print(f"{self.__class__.__name__}: Executing")


class Facade:
    """
    Facade wrapping complex subsystem within a easy to use API.
    It could wrap multiple subsystems or we can create multiple
    facades each with it's own set of responsibilities.
    """

    def __init__(self, source: Optional[str] = ""):
        if source == "a":
            self._sources = {"a": SubSystemA()}
        elif source == "b":
            self._sources = {"b": SubSystemB()}
        else:
            self._sources = {"a": SubSystemA(), "b": SubSystemB()}

    def execute(self, some_variable: Optional[str] = "") -> None:
        if some_variable:
            self._sources[some_variable].execute_me()
        else:
            for source in self._sources.values():
                source.execute_me()


if __name__ == "__main__":
    facade = Facade()
    facade.execute()
