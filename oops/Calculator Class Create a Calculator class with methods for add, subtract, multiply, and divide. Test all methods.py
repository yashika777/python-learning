class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def multiply(self):
        return f'Multiplication of {self.a} and {self.b} is {self.a*self.b}'
    def add(self):
        return f"addition of {self.a} and {self.b} is {self.a+self.b}"
    def sub(self):
        return f"subtraction of {self.a} and {self.b} is {self.a-self.b}"
    def divide(self):
        return f"division of {self.a} and {self.b} is {self.a/self.b}"
c1=Calculator(5,6)
c2=Calculator(8,19)
print(c1.multiply())
print(c1.add())
print(c1.sub())
print(c1.divide())
print(c2.multiply())
print(c2.add())
print(c2.sub())
print(c2.divide())

    
    
