n=input()
l=[i for i in n]
z=len(l)
a=[]
for i in range(len(l)):
    if l.count(l[i])==1:
        a.append(l[i])
if len(a)==z:
    print(True)
else:
    print(False)
        
