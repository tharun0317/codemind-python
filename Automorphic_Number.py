a=int(input())
b=a**2
c=str(b)
if c.endswith(str(a)):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")