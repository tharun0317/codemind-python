n=int(input())
s=list(map(int,input().split()))
x=int(input())
for i in s:
    if x in s:
        print(True)
        break
    else:
        print(False)
        break