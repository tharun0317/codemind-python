def prime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
a=int(input())
b=int(input())
s=a+b
for i in range(1,a+1):
    if prime(i+s)==True:
        print(i)
        break