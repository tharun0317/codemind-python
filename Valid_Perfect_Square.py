n=int(input())
for i in range(n):
    a=int(input())
    f=0
    for i in range(1,int(a*0.5)+1):
        if i*i==a:
            f=1
    if f==1:
        print("True")
    else:
        print("False")