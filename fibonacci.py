n=int(input())
a=0
b=1
z=[0,1]
for i in range(1,n-1):
    c=a+b
    a=b
    b=c
    z.append(b)
print(*z)