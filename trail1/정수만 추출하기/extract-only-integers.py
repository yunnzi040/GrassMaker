A, B = map(str, input().split())
A_int = B_int = ""

for i in A:
    if i.isdigit():
        A_int += i
    else:
        break

for i in B:
    if i.isdigit():
        B_int += i
    else:
        break

print(int(A_int) + int(B_int))