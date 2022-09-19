a=input()
x=[i for i in a]
c=0
d=0
for i in x:
    if i=="o":
        c+=1
    else:
        d+=1
if c==(d*2):
    print("Yes")
else:
    print("No")