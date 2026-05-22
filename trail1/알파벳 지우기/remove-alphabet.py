a = input()
b = input()
a_int = b_int = ""

for i in a:
    if i.isdigit():
        a_int += i

for i in b:
    if i.isdigit():
        b_int += i

print(int(a_int) + int(b_int))
