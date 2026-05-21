N = int(input())

arr_2d = [
    [0 for _ in range(N)]
    for _ in range(N)
]


for i in range(N):
    if i == 0:
        arr_2d[i][0] = 1
    else:
        arr_2d[i][0] = arr_2d[i-1][0] + 1

    for j in range(1, N):
        arr_2d[i][j] = arr_2d[i][j-1] + N

for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()

