password=(input('enter password: '))
uppercase='no' 
lowercase='no'
digit='no'
specialcharcter='no'
if len(password)>=8:
    for i in password:
        if i.isdigit():
            digit='yes'
        if i in '@#&':
            specialcharcter='yes'
        if i.isupper():
            uppercase='yes'
        if i.islower():
            lowercase='yes'
    if uppercase=='yes' and lowercase=='yes' and digit=='yes' and specialcharcter=='yes':
        print('strong')
    elif uppercase=='yes' and lowercase=='yes':
        print('medium')
else:
    print('weak')


            


