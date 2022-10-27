n=int(input())
t=1
a=n
while a:
    for i in range(1,t+1):
        print(i,end="")
    t+=1
    a-=1
    print()