n,m=map(int,input().split())
a=[int(i) for i in input().split()][:n]
b=[int(i) for i in input().split()][:m]
z=list(set(a))
c=0
for i in z:
    if i in b:
        c+=1
print(c)