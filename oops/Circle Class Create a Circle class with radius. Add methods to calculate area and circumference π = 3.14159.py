import math
class Circle:
    def __init__(self,radius):
        self.r=radius
    def area(self):
        return math.pi*self.r**2
    def circumference(self):
        return math.pi*2*self.r
c1=Circle(5)
c2=Circle(8.6)
print(c1.area())
print(c1.circumference())
print(c2.area())
print(c2.circumference())