from dataclasses import dataclass, field
from decimal import Decimal
import math

# ``dataclass`` provides many functionalities automatically
@dataclass
class Point:
    x: float
    y: float
    
    @property
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)
    
@dataclass(frozen=True) 
class Item:
    """
    frozen: inmutable
    """
    name: str
    price: Decimal = Decimal(0)
    colors: str = field(default_factory=list)
    
    @property
    def amount(self):
        return f"€{self.price:,.2f}"
    
if __name__ == "__main__":
    point = Point(x=1, y=1)
    print(point)
    print(point.magnitude)
    
    duck = Item(name='duck', price=5, colors=['purple', 'red'])
    
    