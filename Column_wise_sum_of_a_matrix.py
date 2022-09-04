n,m=map(int,input().split())
mat=[]
for i in range(n):
    l=[int(x) for x in input().split()]
    mat.append(l)
a=[]
b=0
c=0
for i in range(max(n,m)):
    for j in range(n):
        for k in range(m):
            if k==b:
                c+=mat[j][k]
    a.append(c)
    b+=1
    c=0
print(*a)
                
            