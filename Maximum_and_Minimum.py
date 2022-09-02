n=int(input())
a=list(map(int,input().split()))[:n]
b=[]
for i in a:
    if a.count(i)==i:
        b.append(i)
if len(b)!=0:
    print(min(b),max(b))
else:
    print(-1)