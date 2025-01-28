class Shape:
    def area(self, length, width):
        self.length = length
        self.width = width
        raise NotImplementedError("Subclass must implement this method")
class Rectangle(Shape):
    def area(self, length, width):
        return length * width
class Circle(Shape):
    def area(self, radius):
        return π × radius²
