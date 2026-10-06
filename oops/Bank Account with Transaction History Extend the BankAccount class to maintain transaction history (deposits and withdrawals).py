class Bank_account:
    def __init__(self,balance):
        self.history=[]
        self.balance=balance
    def deposit(self):
        dep=int(input('Enter amount deposited:'))
        self.balance+=dep
        self.history.append(f'Deposired ₹{dep}')
        return self.balance
    def withdrawl(self):
        withdraw=int(input("enter amout withdrwan:"))
        if withdraw<self.balance:
            self.balance-=withdraw
        else:
            return'Balance is not sufficient for thus withdrawl'
        self.history.append(f'Withdrawn ₹{withdraw}')
        return self.balance
b1=Bank_account(5000)
print(b1.deposit())
print(b1.withdrawl())
print(b1.history)
    


