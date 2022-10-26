n=int(input())
c=0
a=1
for i in range(1,n+1):
    c=c+1/a
    a+=1
print("%.2f"%c)