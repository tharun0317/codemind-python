n=int(input())
def prime(n):
    if n==1:return False
    for i in range(2,n):
        if n%i==0:return False
    return True
for i in range(2,n):
    if n%i==0 and prime(i)==True and prime(n//i)==True:
        print(i,n//i)
        break
else:
    print(-1)