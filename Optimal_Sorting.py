n=int(input())
for i in range(n):
    m=int(input())
    l=list(map(int,input().split()))[:m]
    a=sorted(l)
    if a==l:
        print(0)
    else:
        print(max(a)-min(a))