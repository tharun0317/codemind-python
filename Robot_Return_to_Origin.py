x=input()
a=[i for i in x]
c=0
y="UR"
for i in a:
    if i in y:
        c+=1
    else:
        c-=1
if c==0:
    print(True)
else:
    print(False)