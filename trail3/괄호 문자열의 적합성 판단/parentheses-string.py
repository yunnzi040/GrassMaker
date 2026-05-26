str = input()

# Please write your code here.
s = []
valid = True

for ch in str:

    if ch == "(":
        s.append(ch)

    else:
        if not s:
            valid = False
            break

        s.pop()

if s:
    valid = False

if valid:
    print("Yes")
else:
    print("No")



