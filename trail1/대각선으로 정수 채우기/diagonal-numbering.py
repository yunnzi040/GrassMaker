n, m = map(int, input().split())

arr_2d = [[0 for _ in range(m)] for _ in range(n)]

num = 1

for s in range(n + m - 1):
    for r in range(n):
        c = s - r

        if 0 <= c < m:
            arr_2d[r][c] = num
            num += 1

for row in arr_2d:
    print(*row)