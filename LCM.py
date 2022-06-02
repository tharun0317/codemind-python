a,b=map(int,input().split())
maxi=max(a,b)
m=maxi
while True:
    if m%a==0 and m%b==0:
        lcm=m
        break
    m=m+maxi
print(lcm)