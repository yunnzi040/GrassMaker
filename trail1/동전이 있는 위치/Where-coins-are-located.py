N, M = map(int, input().split())

arr_2d = [
    [0 for _ in range(N)]
    for _ in range(N)
]

for i in range (M):
    r, c = map(int, input().split())
    arr_2d[r-1][c-1] = 1

for row in arr_2d:
    print(*row)


