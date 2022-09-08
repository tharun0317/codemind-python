n=int(input())
a=[int(i) for i in input().split()][:n]
c=1
for i in range(1,n):
    if a[i]<a[i-1]:
        c+=1
if len(a)==c:
    print("yes")
else:
    print("no")