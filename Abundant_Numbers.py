n=int(input())
a=[]
b=0
for i in range(1,n):
    if n%i==0:
        a.append(i)
for i in a:
    b+=i
if b>n:
    print(True)
else:
    print(False)