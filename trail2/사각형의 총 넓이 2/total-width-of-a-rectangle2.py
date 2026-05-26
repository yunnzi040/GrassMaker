n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
result = [[0 for _ in range(1000)] for _ in range(1000)]
x = 100
y = 100

for i in range(n):

    for x in range(x1[i], x2[i]):
        for y in range(y1[i], y2[i]):
            result[x][y] += 1

cnt = 0
for j in result:
    for i in j:
        if i > 0:
            cnt += 1

print(cnt)