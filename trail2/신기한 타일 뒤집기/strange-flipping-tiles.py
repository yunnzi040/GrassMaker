n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
result = [" "] * 200000
idx = 100000

for i in range(n):
    for j in range(x[i]):
        if dir[i] == "R":
            result[idx] += "B"

            if j != x[i] - 1:
                idx += 1
        else:
            result[idx] += "W"

            if j != x[i] - 1:
                idx -= 1

black = 0
white = 0

for tile in result:
    if tile[-1] == "B":
        black += 1
    elif tile[-1] == "W":
        white += 1

print(white, black)

