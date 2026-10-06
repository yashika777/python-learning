class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
class Square(Shape):
    def __init__(self,s):
        self.s=s
    def area(self):
        return  self.s**2
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return  3.14*self.r**2
       
class Triangle(Shape):
    def __init__(self,b,h):
        self.b=b
        self.h=h
    def area(self):
         return (self.b*self.h)*(1/2)

sh1=Rectangle(4,8)
print(sh1.area())

sh2=Square(8)
print(sh2.area())
sh3=Circle(4)
print(sh3.area())
sh4=Triangle(4,8)
print(sh4.area())

