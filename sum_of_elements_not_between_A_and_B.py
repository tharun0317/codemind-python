n=int(input())
s=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
for i in range(len(s)):
    if s[i]<a or s[i]>b:
        c+=s[i]
print(c)