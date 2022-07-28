a=int(input())
b=list(str(a))
s=0
p=1
for i in range(len(b)):
    s=s+int(b[i])
    p=p*int(b[i])
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")
    