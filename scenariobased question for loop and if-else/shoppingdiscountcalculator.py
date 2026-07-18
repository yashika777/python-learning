shopping=int(input('enter purchase amount:'))
discount=0
if shopping<=1000:
    print('no discount!!!')
    discount=0
elif 1000<shopping<=5000:
    discount=shopping*0.10
elif 5000<shopping<=10000:
    discount=shopping*0.20
elif shopping>10000:
    discount=shopping*0.30
print(shopping-discount)
