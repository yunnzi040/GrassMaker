N = int(input())

arr_2d = [
    [0 for _ in range(N)]
    for _ in range(N)
]

# 첫번째 행과 첫번째 열에는 모두 1이 들어간다.
for i in range(N):
    arr_2d[i][0] = 1
    arr_2d[0][i] = 1

# 나머지 칸들은 바로 위의 값([i-1][j])과 바로 왼쪽 값([i][j-1]) 그리고 
# 왼쪽 위의 값([i-1][j-1])의 합이 되어야 한다.
for i in range(1, N):
    for j in range(1, N):
        arr_2d[i][j] = arr_2d[i-1][j] + arr_2d[i][j-1] + arr_2d[i-1][j-1]

for row in arr_2d:
    print(*row)
