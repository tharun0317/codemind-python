n=int(input())
t=n
a=1
while t:
    for i in range(a,n+1):
        print(i,end=" ")
    a+=1
    t-=1
    print()
    