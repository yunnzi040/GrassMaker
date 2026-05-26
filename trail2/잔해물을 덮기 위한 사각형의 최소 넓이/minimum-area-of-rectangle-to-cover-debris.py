x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.
OFFSET = 1000
SIZE = 2001

arr = [[0] * SIZE for _ in range(SIZE)]

for i in range(2):
    for x in range(OFFSET + x1[i], OFFSET + x2[i]):
        for y in range(OFFSET + y1[i], OFFSET + y2[i]):
            if i == 0:
                arr[x][y] = 1
            else:
                arr[x][y] = 0

min_x = min_y = SIZE
max_x = max_y = -1

for x in range(SIZE):
    for y in range(SIZE):
        if arr[x][y] == 1:
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

if max_x == -1:
    print(0)
else:
    print((max_x - min_x + 1) * (max_y - min_y + 1))