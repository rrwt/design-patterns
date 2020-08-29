"""
Example: Fit square pegs in round holes
"""
from math import sqrt


class RoundPeg:
    def __init__(self, radius) -> None:
        self._radius = radius

    @property
    def radius(self) -> int:
        return self._radius


class RoundHole:
    def __init__(self, radius: int) -> None:
        self._radius = radius

    @property
    def radius(self) -> int:
        return self._radius

    def fits(self, peg: RoundPeg) -> bool:
        """
        Whether a peg fits a hole
        """
        return peg.radius <= self.radius


class SquarePeg:
    def __init__(self, side: int) -> None:
        self._side = side

    @property
    def side(self) -> int:
        return self._side


class SquarePegAdapter(RoundPeg):
    def __init__(self, peg: SquarePeg) -> None:
        self._peg = peg
        super().__init__(self.radius)

    @property
    def radius(self) -> float:
        return self._peg.side / sqrt(2)


if __name__ == "__main__":
    round_peg = RoundPeg(radius=10)
    round_hole = RoundHole(radius=10)
    print(
        f"Round peg with radius {round_peg.radius} fits "
        f"round hole with radius {round_hole.radius}?",
        round_hole.fits(round_peg),
    )

    square_peg = SquarePeg(side=13)
    square_peg_adapter = SquarePegAdapter(square_peg)
    print(
        f"Square peg with side {square_peg.side} fits "
        f"round hole with radius {round_hole.radius}?",
        round_hole.fits(square_peg_adapter),
    )
