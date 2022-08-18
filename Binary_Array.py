n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if i==0 or i==1:
        b.append(i)
if len(b)==len(a):
    print(True)
else:
    print(False)