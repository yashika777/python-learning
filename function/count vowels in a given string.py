def stri(n):
    count=0
    for i in n:
        if i in ('a','e','i','o','u','A','E','I','O','U'):
            count+=1
    return count
n=input('enter string:')
print(stri(n))
