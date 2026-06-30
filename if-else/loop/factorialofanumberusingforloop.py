n=int(input('enter number:'))
j=1
for i in range(1,n+1):
    if i<n+1:
        j*=i
print(j)