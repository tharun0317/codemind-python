a=input()
x=[i for i in a]
c="1234567890"
y=[i for i in c]
d=0
for i in x:
    if i in y:
        d+=int(i)
print(d)