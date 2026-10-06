def gcd(n,m):
    gc=0
    for i in range(1,min(n,m)+1):
        if n%i==0 and m%i==0:
            gc=i
            if n//i!=i:
                gc=i
    print(gc)
gcd(40,16)

    




            
