a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def four_basic_operations(a,s,c):
    if s == '+' :
        return a + c
    elif s == '-':
        return a - c
    elif s == '/':
        return a // c
    elif s == '*':
        return a * c
    else:
        return False

result = four_basic_operations(a, o, c)

if result is not False:
    print(f"{a} {o} {c} = {result}")
else:
    print(False)
