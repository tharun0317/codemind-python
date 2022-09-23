n=int(input())
a=0
b=1
z=[0,1]
for i in range(1,n):
    c=a+b
    a=b
    b=c
    z.append(b)
if n in z:
    print(True)
else:
    print(False)