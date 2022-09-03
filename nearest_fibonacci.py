n=int(input())
a=0
b=1
c=a+b
while n>=c:
    a=b
    b=c
    c=a+b
if (n-b)>(c-n):
    print(c)
elif (n-b)<(c-n):
    print(b)
else:
    print(b,c)
