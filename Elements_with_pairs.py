n=int(input())
a=list(map(int,input().split()))[:n]
if len(a)%2!=0:
    a.append("0")
print(*a)