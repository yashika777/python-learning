# perfectnumber:if the number is equal to sum of its proper divisors excluding itself
# def perfect_number(n,i):
#     if (i==n):
#         return 0
#     if n%i==0:
#         return i+perfect_number(n,i+1)
#     else:
#         return perfect_number(n,i+1)
# def sum(n):
#     if perfect_number(n,1)==n:
#         print('is perfect number')
#     else:
#         print('not a perfect number')
# sum(2)
def recu(i,n):
    if i>n:
        return
    else:
        print(i)
        recu(i+1,n)
recu(1,7)