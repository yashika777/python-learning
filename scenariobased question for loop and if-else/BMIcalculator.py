weight=float(input('enter in kg :'))
height=float(input('enter in m :'))
BMI=float(weight/(height**2))
if BMI<=18.5:
    print('Underweight',BMI)
elif BMI<25:
    print('Normal',BMI)
elif BMI<30:
    print('Overweight',BMI)
else:
    print('obese',BMI)