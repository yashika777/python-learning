class Employee:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
    def increment(self):
        self.salary+=self.salary*0.1
        return f"{self.name}'s new salary is  {self.salary}"
emp1=Employee('Yashika',499,50000)
emp2=Employee('Swasti',368,65000)
print(emp1.increment())
print(emp2.increment())