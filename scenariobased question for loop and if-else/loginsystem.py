password=input('enter password')
for i in range(3):
    check=input('enter password')
    if password==check:
        print('✅successful')
        break
    else:
        print('incorrect',2-i ,'attempts are left')
    
if password!=check:
    print('your attempts are finished')

