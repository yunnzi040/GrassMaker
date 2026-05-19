num = int(input())
count = 0
i = 1
arr = []

while (True):
    value = num * i
    arr.append(value)

    if value % 5 == 0:
        count += 1

    if count == 2:
        break
    
    i += 1

print(*arr)



