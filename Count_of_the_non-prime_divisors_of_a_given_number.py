n=int(input())
def is_prime(a):
    fc=0
    for i in range(1,a+1):
        if a%i==0:
            fc+=1
    if fc==2:
        return True
    else:
        return False
a=[]
for i in range(1,n+1):
    if n%i==0:
        a.append(i)
count=0
for i in a:
    if is_prime(i)==False:
        count+=1
print(count)