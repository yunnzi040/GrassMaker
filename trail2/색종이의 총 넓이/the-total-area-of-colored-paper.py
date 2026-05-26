n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
arr = [[0] * 1001 for _ in range(1001)]
x_idx = 100
y_idx = 100

for a in range(n):
    for i in range(x_idx + x[a], x_idx + x[a] + 8):
        for j in range(y_idx + y[a], y_idx + y[a] + 8):
            arr[i][j] += 1

cnt = 0

for a in arr:
    for b in a:
        if b > 0 :
            cnt += 1

print(cnt)


