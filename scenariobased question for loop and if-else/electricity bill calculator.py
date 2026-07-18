unit=int(input('enter unit used:'))
bill=0
if unit<=100:
    bill=unit*5
elif 101<=unit<=200:
    bill=100*5
    bill+=(unit-100)*7
elif unit>200:
    bill=100*5
    bill+=100*7
    bill+=(unit-200)*10
print(bill)