arr = list(input())
c = arr[0]
o = arr[1]

for i in range(len(arr)):
    if arr[i] == c : # c랑 같으면
        arr[i] = o
    elif arr[i] == o: # o랑 같으면
        arr[i] = c

print("".join(arr))


