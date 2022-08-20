n=int(input())
b=n
def rev(n):
    a=0
    while n>0:
        r=n%10
        a=a*10+r
        n=n//10
    return a
def tha(n):
    a=0
    i=1
    while n>0:
        r=n%10
        a=a+r**i
        n=n//10
        i+=1
    return a
if (tha(rev(n)))==b:
    print(True)
else:
    print(False)

        