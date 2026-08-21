def isprime(n):
    factor=0
    for i in range(2,n):
        if n%i==0:
            factor+=1
    if factor==0:
        print(f'{n} is a prime number')
    else:
        print(f'{n} is not a prime number')
n=int(input('enter a number:'))
isprime(n)


        

    