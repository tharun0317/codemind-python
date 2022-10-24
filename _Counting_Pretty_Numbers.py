n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    c=0
    for i in range(a,b+1):
        if str(i).endswith("2") or str(i).endswith("3") or str(i).endswith("9"):
            c+=1
    print(c)