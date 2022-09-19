n=int(input())
m=list(map(int,input().split()))[:n]
m.sort()
print(*m)