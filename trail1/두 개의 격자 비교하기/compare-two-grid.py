N, M = map(int, input().split())

arr_2d1 = [
    list(map(int, input().split()))
    for _ in range(N)
]

arr_2d2 = [
    list(map(int, input().split()))
    for _ in range(N)
]

result = [
    [0 for _ in range(M)]
    for _ in range(N)
]

for i in range(N):
    for j in range(M):
        if arr_2d1[i][j] != arr_2d2[i][j]:
            result[i][j] = 1
        else:
            result[i][j] = 0

for row in result:
    for elem in row:
        print(elem, end=" ")
    print()