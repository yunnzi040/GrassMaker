N = int(input())
arr_2d = [
    [0 for _ in range(N)]
    for _ in range(N)
]

for i in range(N):
    for j in range(i+1):
        # 첫번째 수, 각 줄의 마지막 수에 1을 넣기
        if j == 0 or j == i:
            arr_2d[i][j] = 1
        else:
            arr_2d[i][j] = arr_2d[i-1][j-1]+arr_2d[i-1][j]


for row in arr_2d:
    for elem in row:
        if elem == 0:
            print(" ", end=" ")
        else:
            print(elem, end=" ")
    print()

