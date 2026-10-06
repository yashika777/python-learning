class Counter:
    def __init__(self,count):
        self.count=count
    def increment(self):
        self.count+=1
        return self.count
    def decrement(self):
        self.count-=1
        return self.count
    def reset(self):
        self.count=0
        return self.count
c1=Counter(10)
print(c1.decrement())
print(c1.increment())
print(c1.reset())

