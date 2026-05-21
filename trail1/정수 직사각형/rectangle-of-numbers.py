# 세로변 N, 가로변 M
N, M = map(int, input().split())
start = 1

arr_2d = [
    [0 for _ in range(M)]
    for _ in range(N)
]

for i in range(N):
    for j in range(M):
        arr_2d[i][j] = start
        start += 1

for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()


