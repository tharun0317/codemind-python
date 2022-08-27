def rev(n):
    a=0
    while n>0:
        r=n%10
        a=a*10+r
        n=n//10
    return a
def prime(n):
    if n==1:return False
    for i in range(2,n):
        if n % i==0:return False
    return True
n=int(input())
if prime(n)==True:
    if prime(rev(n))==True:
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")