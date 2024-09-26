from typing import Protocol


class CalculatePerimeter(Protocol):
    def calculate_perimeter(self) -> float: ...


class Square(CalculatePerimeter):
    def __init__(self, side: float) -> None:
        self.side = side

    def calculate_perimeter(self) -> float:
        return self.side * 4


square = Square(5)
print(square.calculate_perimeter())
