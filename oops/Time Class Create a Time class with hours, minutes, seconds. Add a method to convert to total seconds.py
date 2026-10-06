class Time:
    def __init__(self,Hour,Minute,Seconds):
        if Hour<0 or Hour>23:
           raise ValueError('Invalid')
        elif Minute>=60 or Seconds>=60 or Minute<0 or Seconds<0:
            raise ValueError('invalid')   
        self.hour=Hour
        self.minute=Minute
        self.seconds=Seconds
    def total_seconds(self):
        totalsecomds=self.hour*60*60+self.minute*60+self.seconds
        return totalsecomds
t1=Time(3,45,57)
t2=Time(10,56,70)
print(t1.total_seconds())
print(t2.total_seconds())