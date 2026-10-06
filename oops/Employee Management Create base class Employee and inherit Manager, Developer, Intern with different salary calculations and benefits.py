# class Employee:
#     def salary(self):
#         pass
#     def benefits(self):
#         pass
# class Manager(Employee):
#     def __init__(self,basesalary,bonus):
#         self.bs=basesalary
#         self.bonus=bonus
#     def salary(self):
#         return self.bs+self.bonus
#     def benefits(self):
#         return 'Health insurance' , 'Travel expenses'
# class Developer(Employee):
#     def __init__(self,basesalary,bonus):
#         self.bs=basesalary
#         self.bonus=bonus
#     def salary(self):
#         return self.bs+self.bonus
#     def benefits(self):
#         return 'Travel expenses covered'
# class Intern(Employee):
#     def __init__(self,stipend):
#         self.st=stipend
#     def salary(self):
#         return self.st
#     def benits(self):
#         return 'chances of getting ppo'
# e1=Manager(65000,5000)
# print(e1.salary())
# for i,benefits in enumerate(e1.benefits(),start=1):
#     print(f"{i}. {benefits}")
# e2=Developer(55000,2000)
# print(e2.salary())
# print(e2.benefits())
# e3=Intern(45000)
# print(e3.salary())
# print(e3.benefits())
count=0
def rec():
    global count
    if count==4:
        return
    else:
        count+=1
        print(count)
        rec()
rec()
    











    


      

        
        


