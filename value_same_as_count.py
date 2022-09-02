n=int(input())
a=list(map(int,input().split()))[:n]
b=[]
for i in a:
    if a.count(i)==i and i not in b:
        b.append(i)
print(len(b))
 