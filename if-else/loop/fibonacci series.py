a=0
b=1
i=int(input('enter range:'))
n=1
while n<=i:
    print(a)
    a,b=b,a+b
    n+=1
a=0
b=1
for i in range(1,10):
    print(a)
    a,b=b,a+b
