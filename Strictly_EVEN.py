n=int(input())
a=list(map(int,input().split()))
cont=0
for i in range(len(a)):
    if a[i]%2==0 and i%2==0 :
        cont+=1
z=[]
for i in a:
    if i%2==0:
        z.append(i)
if cont>=len(z):
    print (True)
else:
    print(False)