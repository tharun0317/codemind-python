n=int(input())
a=0
b=n
while n>0:
    r=n%10
    a=a*10+r
    n=n//10
if a==b:
    print(True)
else:
    print(False)
