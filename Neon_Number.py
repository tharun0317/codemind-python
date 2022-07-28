a=int(input())
b=a**2
c=list(str(b))
s=0
for i in range(len(c)):
    s=s+int(c[i])
if s==a:
    print("Neon Number")
else:
    print("Not Neon Number")
    