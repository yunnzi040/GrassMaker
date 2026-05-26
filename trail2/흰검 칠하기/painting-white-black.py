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
    for _ in range(x[i]):
        if dir[i] == "R":
            result[idx] += "B"

            if _ != x[i] - 1:
                idx += 1
        else:
            result[idx] += "W"

            if _ != x[i] - 1:
                idx -= 1
black = 0
white = 0
gray = 0

for i in result:
    if i.count("B") >= 2 and i.count("W") >= 2:
        gray += 1
    else :
        if i[-1] == "B":
            black += 1
        elif i[-1] == "W":
            white += 1

print(white, black, gray)
    