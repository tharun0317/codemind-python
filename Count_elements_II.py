n,m=map(int,input().split())
a=list(map(int,input().split()))[:n]
b=list(map(int,input().split()))[:m]
c=[]
for i in list(set(a)):
    if i not in b:
        c.append(i)
for i in list(set(b)):
    if i not in a and i not in c:
        c.append(i)
print(len(c))
