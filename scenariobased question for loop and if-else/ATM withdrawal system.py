a=int(input('enter amount to be withdrawan:'))
balance=int(input('enter balance:'))
if a<=balance:
    if a%100==0:
        if balance-a>=500:
            balance-=a
        else:
            print('minimum amount is not maintained')
    else:
        print('amoubt should be multiple of 100!!!')

else:
    print('insufficient balance!!!')
print(balance)