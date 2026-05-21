N, M = map(int, input().split())

arr_2d = [
    [0 for _ in range(N)]
    for _ in range(N)
]

for i in range(M):
    a, b = map(int, input().split())
    arr_2d[a-1][b-1] = a * b
        
    
for row in arr_2d:
    print(*row)