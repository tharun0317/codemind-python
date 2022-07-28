a,b=map(int,input().split())
c=max(a,b)
d=min(a,b)
m=c
while True:
    if m%d==0:
        print(m)
        break
    else:
        m+=c
        