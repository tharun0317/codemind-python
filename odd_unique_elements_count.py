n=int(input())
a=list(map(int,input().split()))[:n]
b=list(set(a))
z=0
for i in b:
    if i%2!=0:
        z+=1
print(z)