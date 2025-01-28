import math
class Shape:
    def area(self, length, width):
        self.length = length
        self.width = width
        raise NotImplementedError("Subclass must implement this method")
class Rectangle(Shape):
    def __init__(self, length, width):
        return self.length * self.width
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        return π * self.radius ** 2
