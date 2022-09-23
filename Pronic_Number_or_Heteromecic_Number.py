n=int(input())
f=0
for i in range(1,n+1):
    if n%i==0 and n//i==i+1:
        f=1
if f==1:
    print("YES")
else:
    print("NO")