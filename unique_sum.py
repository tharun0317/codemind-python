n=int(input())
a=list(map(int,input().split()))[:n]
b=list(set(a))
z=0
for i in b:
    z+=i
print(z)