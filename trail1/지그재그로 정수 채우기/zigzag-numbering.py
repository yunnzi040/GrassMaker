n, m = map(int, input().split())

# Please write your code here.
arr_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]

num = 0

for j in range(m):      # 열 기준으로 이동
    if j % 2 == 0:
        # 위에서 아래로
        for i in range(n):
            arr_2d[i][j] = num
            num += 1
    else:
        # 아래에서 위로
        for i in range(n - 1, -1, -1):
            arr_2d[i][j] = num
            num += 1

for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()