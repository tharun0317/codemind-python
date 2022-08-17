n=int(input())
x=list(map(int,input().split()))
a=[]
b=[]
c=[]
for i in x:
    if i%2==0:
        a.append(i)
    else:
        b.append(i)
for i in b:
    c.append(i)
for i in a:
    c.append(i)
print(*c)