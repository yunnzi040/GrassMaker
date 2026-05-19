check = [0 for _ in range(4)]

for _ in range (3):
    arr = list(map(str, input().split()))
    
    if arr[0] == "N": 
        if int(arr[1]) >= 37:
            check[1] += 1
        else:
            check[3] += 1

    elif arr[0] == "Y":
        if int(arr[1]) >= 37:
            check[0] += 1
        else:
            check[2] += 1
    
if check[0] >= 2:
    print(*check, "E")
else:
    print(*check)

    