n,m=map(int,input().split())
a=list(map(int,input().split()))[:n]
b=list(map(int,input().split()))[:m]
c=[]
for i in a:
    if i not in b:
        c.append(i)
for i in b:
    if i not in a and i not in c:
        c.append(i)
print(*c)
