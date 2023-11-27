class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

def area(rectangle: Rectangle) -> float:
    return rectangle.width * rectangle.height

def test_rectangle() -> None:
    rectangle = Rectangle(4, 3)
    assert rectangle.width == 4
    assert rectangle.height == 3
    assert area(rectangle) == 12

# Run the test
test_rectangle()
