n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]

# Please write your code here.
class Point:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num

pointss = [Point(points[i][1][0], points[i][1][1], points[i][0]) for i in range(n)]

pointss.sort(key=lambda a: (abs(a.x) + abs(a.y)))

for p in pointss:
    print(p.num+1)