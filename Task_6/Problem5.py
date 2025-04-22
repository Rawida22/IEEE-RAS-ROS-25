from math import pi
class Shape:
    def __init__(self):
        pass
    def area(self):
        pass
    def perimeter(self):
        pass

class  Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius =   radius
    def area(self):
        return  pi* self.radius* self.radius 
    def perimeter(self):
        return 2 *pi* self.radius  
Circle1 = Circle(7)
print(f"Circle Area:{Circle1.area()}")
print(f"Circle Perimeter:{Circle1.perimeter()}\n") 

class Rectangle(Shape):
    def __init__(self, Length,Width):
        super().__init__()
        self.Length = Length
        self.Width = Width
    def area(self):
        return self.Length * self.Width
    def perimeter(self):
        return 2*(self.Length + self.Width)
Rectangle1 = Rectangle(5,7)
print(f"Rectangle Area:{Rectangle1.area()}")
print(f"Rectangle Perimeter:{Rectangle1.perimeter()}\n")

class Triangle (Shape):
    def __init__(self,Base,Height,side1,side2,side3):
        super().__init__()
        self.Base = Base
        self.Height = Height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def area(self):
        return 0.5*self.Base*self.Height
    def perimeter(self):
        return self.side1 + self.side2  + self.side3 
Triangle1 = Triangle(5,4,4,3,5)
print(f"Triangle Area:{Triangle1.area()}")
print(f"Triangle perimeter:{Triangle1.perimeter()}\n")