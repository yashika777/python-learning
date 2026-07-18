age=int(input('enter age:'))
day=input('if weekend(saturday,sunday):')
price=0
if age<12:
    price=100
elif age>=60:
    price=150
else:
    price=200
if day=='yes':
    price+=50
print(price)


