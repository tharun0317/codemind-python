a=int(input())
b=list(map(int,input().split()))
c=0
for i in b:
    if i%2==0:
        c+=1
if len(b)==c:
    print("True")
else:
    print("False")