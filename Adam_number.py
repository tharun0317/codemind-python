n=int(input())
a=n**2
def rev(n):
    a=0
    while n>0:
        r=n%10
        a=a*10+r
        n=n//10
    return a
b=rev(rev(n)**2)
if a==b:
    print(True)
else:
    print(False)