arr = list(map(int, input().split(" ")))


for i in range (2,10):
    arr.append(arr[-1] + arr[-2])

new_arr = [arr[i] % 10 for i in range(len(arr))]
print(*new_arr)


