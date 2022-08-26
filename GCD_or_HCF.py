n,m=map(int,input().split())
a=[]
b=[]
c=[]
for i in range(1,n+1):
    if n%i==0:
        a.append(i)
for i in range(1,m+1):
    if m%i==0:
        b.append(i)
for i in range(max(n,m)):
    if i in a and i in b:
        c.append(i)
print(c.pop())