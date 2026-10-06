class Person:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
    def adult_or_not(self):
        if self.age>18:
            return f"{self.name} is adult"
        else:
            return f"{self.name} is not adult"
p1=Person("Yashika",19,"Sirsa")
p2=Person("Ishant",17,"Sirsa")
print(p1.adult_or_not())
print(p2.adult_or_not())