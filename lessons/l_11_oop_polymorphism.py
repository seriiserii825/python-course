def l_11_oop_polymorphism():
    class Shape:
        def calc_area(self):
            raise NotImplementedError("This method should be overridden in subclasses")

    class Circle(Shape):
        def __init__(self, radius: float) -> None:
            self.radius = radius

        def calc_area(self):
            return 3.14 * self.radius ** 2

    class Rectangle(Shape):
        def __init__(self, width: float, height: float) -> None:
            self.width = width
            self.height = height

        def calc_area(self):
            return self.width * self.height

    shapes = [
        Circle(radius=5),
        Rectangle(width=4, height=6)
            ]
    for shape in shapes:
        print(f"Area: {shape.calc_area()}")
