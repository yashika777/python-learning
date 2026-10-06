class Rectangle:
    def __init__(self,length,width):
        self.l=length
        self.w=width
    def area(self):
        return self.l*self.w
    def perimeter(self):
        return 2*(self.l+self.w)
r1=Rectangle(5,8)
r2=Rectangle(9,8.5)
r3=Rectangle(13,24)
print(r1.area())
print(r1.perimeter())
print(r2.area())
print(r2.perimeter())
print(r3.area())
print(r3.perimeter())