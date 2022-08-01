n=int(input())
def happy_number(n):
    a=0
    while n>0:
        r=n%10
        a=a+r**2
        n=n//10
    return a
while n>7:
    n=happy_number(n)
if n==1 or n==7:
    print("True")
else:
    print("False")
