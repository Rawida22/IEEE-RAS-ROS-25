from math import pi
class Circle:
     def __init__(self,radius):
        self.radius = radius 

     def area(self):
       return pi* self.radius* self.radius
     def perimeter(self):
       return 2 *pi* self.radius
     
Circle1 = Circle(4)
print(Circle1.area())
print(Circle1.perimeter())