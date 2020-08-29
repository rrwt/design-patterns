"""
Class Adapter:
    This implementation uses inheritance: the adapter
    inherits interfaces from both objects at the same
    time. Only available in languages supporting
    multiple inheritance.
"""
from abc import ABCMeta, abstractmethod
from math import pi


class CircleService:
    """
    Circle Service. All thing circles
    """

    def __init__(self, radius: float) -> None:
        self.radius = radius

    @property
    def circumference(self) -> float:
        """
        Given the radius, calculate the circumference of a circle.
        C = 2 * pi * r
        """
        return 2 * pi * self.radius

    @property
    def area(self) -> float:
        """
        Given the radius, calculate the area
        A = pi * r * r
        """
        return pi * self.radius * self.radius


class SphereInterface(metaclass=ABCMeta):
    """
    Existing interface working with spheres
    """

    @abstractmethod
    def surface_area(self) -> float:
        """
        given radius, get surface area of sphere
        SA = 4 * pi * r * r
        """
        pass

    @abstractmethod
    def volume(self) -> float:
        """
        Given the radius, get the volume
        V = 4 * pi * r * r * r / 3
        """
        pass


class Sphere(CircleService, SphereInterface):
    def _convert_circumference_to_surface_area(self, circumference: float) -> float:
        return circumference * 2 * self.radius

    def _convert_area_to_volume(self, area: float) -> float:
        return area * 4 * self.radius / 3

    def surface_area(self) -> float:
        return self._convert_circumference_to_surface_area(self.circumference)

    def volume(self) -> float:
        return self._convert_area_to_volume(self.area)


if __name__ == "__main__":
    sphere = Sphere(10)
    print("Surface area of sphere:", sphere.surface_area())
    print("Volume of sphere:", sphere.volume())
