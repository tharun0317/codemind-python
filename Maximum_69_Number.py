a=int(input())
b=list(str(a))
for i in range(len(b)):
    if b[i]=="6":
        b[i]="9"
        break
print("".join(b))