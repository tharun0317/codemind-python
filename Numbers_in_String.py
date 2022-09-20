n=input()
a=[i for i in n]
c="1234567890"
cnt=0
for i in a:
    if i in c:
        cnt+=int(i)
print(cnt)