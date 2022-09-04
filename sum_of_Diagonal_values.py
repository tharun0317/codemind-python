n,m=map(int,input().split())
mat=[]
for i in range(n):
    a=list(map(int,input().split()))
    mat.append(a)
add=0
for i in range(n):
    for j in range(m):
        if i==j or i+j==n-1:
            add+=mat[i][j]
print(add)