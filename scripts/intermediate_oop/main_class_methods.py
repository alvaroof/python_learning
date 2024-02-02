
import math

class Circle:
    """Circle with radius, area, etc."""

    def __init__(self, radius=1):
        self.radius = radius

    @property
    def area(self):
        area = math.pi * self.radius**2
        return area

    @property
    def diameter(self):
        diameter = self.radius * 2
        return diameter

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2
        
    @classmethod # Typically used Alternative creation class methods, different from __init__ 
    def from_area(cls, area):
        radius = math.sqrt(area / math.pi) 
        return cls(radius=radius)


if __name__ == '__main__':
    circle = Circle.from_area(area=100)
    print(circle.radius)
    print(circle.diameter)
    print(circle.area)