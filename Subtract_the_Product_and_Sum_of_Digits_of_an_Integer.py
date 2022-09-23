def s_p_d(n):
    a=0
    b=1
    while n>0:
        r=n%10
        a=a+r
        b=b*r
        n=n//10
    return b-a
n=int(input())
print(s_p_d(n))