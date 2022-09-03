n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
for i in range((n//2)+1):
     b.append(i)
for i in a:
    if i not in b:
        c.append(i)
print(sum(b))
print(sum(c))