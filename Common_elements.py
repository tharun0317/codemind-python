n,m=map(int,input().split())
a=[int(i) for i in input().split()][:n]
b=[int(i) for i in input().split()][:m]
c=[]
for i in a:
    if i in b and i not in c:
        c.append(i)
print(*c)