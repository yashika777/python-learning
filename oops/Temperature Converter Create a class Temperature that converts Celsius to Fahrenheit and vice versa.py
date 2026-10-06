class Temperature:
    def __init__(self,temp,type):
        self.temp=temp
        self.type=type
    def conversion(self):
        self.type=self.type.strip().lower()
        if self.type=='celsius':
            return (self.temp*1.8)+32,'Fahrenheit'
        elif self.type=='fahrenheit':
            return (self.temp-32)*(5/9),'Celsius'
        else:
            return 'Invalid type'
t1=Temperature(345,'celsius')
t2=Temperature(876,'fahrenheit')
t3=Temperature(7568,'Tempe')
print(t1.conversion())
print(t2.conversion())
print(t3.conversion())