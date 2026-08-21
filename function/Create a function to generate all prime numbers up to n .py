def prime(n):
    for i in range(2,n):
        factor=0
        for j in range(1,i):
            if i%j==0:
                factor+=1
        if factor==1:
            print(i)
prime(9)
    

    