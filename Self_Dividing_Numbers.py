n=int(input())
s=int(input())
def self_div_num(n):
    f=1
    for i in str(n):
        if i=='0' or n%int(i)>0:
            f=0
    return f
for i in range(n,s+1):
    if self_div_num(i)==1:
        print(i,end=' ')