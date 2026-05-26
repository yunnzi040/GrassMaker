n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
OFFSET = 1000
SIZE = 2001

arr = [[0] * SIZE for _ in range(SIZE)]

for i in range(n):
    for x in range(OFFSET + x1[i], OFFSET + x2[i]):
        for y in range(OFFSET + y1[i], OFFSET + y2[i]):
            if i % 2 == 0: # 빨간색으로 칠하기
                arr[x][y] = 1
            else: # 파란색으로 칠하기
                arr[x][y] = 2

blue = 0

for x in range(SIZE):
    for y in range(SIZE):
        if arr[x][y] == 2:
            blue += 1

print(blue)