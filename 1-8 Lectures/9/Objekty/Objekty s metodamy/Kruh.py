import math

class Circle:

    def __init__(self, center: tuple[float, float], radius: float) -> None:
        self.center = center
        self.radius = radius

    def get_perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def get_area(self) -> float:
        return math.pi * self.radius ** 2

    def __str__(self) -> str:
        return f"Circle at {self.center} with radius {self.radius}"

def test_circle() -> None:
    circle = Circle((-130, -130), 100)
    assert str(circle) == "Circle at (-130, -130) with radius 100"
    assert math.isclose(circle.get_area(), 31415.926535897932, rel_tol=1e-9)

# Run the test
test_circle()
