arr = list(map(int, input().split(" ")))
new_arr = []
for a in arr:
    if a == 0:
        break
    elif a % 2 == 1:
        new_arr.append(a+3)
    elif a % 2 == 0:
        new_arr.append(int(a/2))

print(*new_arr)

