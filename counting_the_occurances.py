n=input()
b=input()
a=[i for i in n]
c=0
for i in a:
    if i==b:
        c+=1
if c==0:
    print(-1)
else:
    print(c)