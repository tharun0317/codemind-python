n,m=map(int,input().split())
mat=[]
for i in range(n):
    a=list(map(int,input().split()))
    mat.append(a)
add=0
for i in range(1,n-1):
    for j in range(1,m-1):
        add+=mat[i][j]
print(add)