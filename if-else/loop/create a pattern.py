"""
*
**
***
****
*****
"""
# n=int(input('enter pattern number:'))
# for i in range(1,n+1):
#     print('*'*i,)
"""
1
23
456
78910
"""
n=int(input('enter number:'))
i=1
num=1
while i<=n:
    j=1
    while j<=i:
        print(num,end='')
        num+=1
        j+=1
    print()
    i+=1   
  
 