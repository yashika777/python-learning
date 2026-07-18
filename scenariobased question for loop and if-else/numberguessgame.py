import random
number=random.randint(1,100)
for i in range(7):
    guess=int(input('enter number:'))
    if guess>100:
        print('please enter vaild number')
        break
    if guess>number:
        print('HINT: lower',6-i,'attempts left')
    elif guess<number:
        print('HINT: higher',6-i,'attempts left')
    else:
        print('You won')
        break
if guess!=number:
    print('You lose',number , 'this is the number')