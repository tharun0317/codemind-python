def palin(n):
    a=0
    while n>0:
        r=n%10
        a=a*10+r
        n=n//10
    return a
n=int(input())
for i in range(n):
    a=int(input())
    if a==palin(a):
        print(True)
    else:
        print(False)
