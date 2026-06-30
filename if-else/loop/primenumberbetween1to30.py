count=0
n=1
while count<10:
    factors=0
    for i in range(1,n+1):
        if n%i==0:
            factors+=1
    if factors==2:
        print(n)
        count+=1
    n+=1

    



