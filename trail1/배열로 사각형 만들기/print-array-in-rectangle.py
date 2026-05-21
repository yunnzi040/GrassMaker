arr_2d = [
    [0 for _ in range(5)]
    for _ in range(5)
]

# 첫 번째 행과 첫 번째 열은 모두 1로 초기화
for i in range(5):
    arr_2d[0][i] = 1
    arr_2d[i][0] = 1

for i in range(1, 5):
    for j in range(1, 5):
        arr_2d[i][j] = arr_2d[i][j-1] + arr_2d[i-1][j]

for row in arr_2d:
    print(*row)
