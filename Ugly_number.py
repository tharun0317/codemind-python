def is_ugly(N):
    while N % 2 == 0:
        N = N // 2
    if N == 1:
        return True
    while N % 3 == 0:
        N = N // 3
    if N == 1:
        return True
    while N % 5 == 0:
        N = N // 5
    if N == 1:
        return True
    return False
n=int(input())
if is_ugly(n)==True:
    print("Ugly Number")
else:
    print("Not Ugly Number")