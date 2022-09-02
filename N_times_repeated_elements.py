n=int(input())
a=list(map(int,input().split()))[:n]
x=int(input())
b=[]
for i in a:
    if a.count(i)==x and i not in b:
        b.append(i)
if len(b)==0:
    print(-1)
else:
    print(*b)