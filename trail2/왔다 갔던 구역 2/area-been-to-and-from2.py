n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
# x는 이동해야 하는 수, dir은 방향
result = [0] * 2000 # 기준점이 idx = 20
idx = 1000 # 이전 인덱스 값을 저장

for i in range(n):
    for _ in range(x[i]):
        if dir[i] == "R":
            result[idx] += 1
            idx += 1
        else:
            idx -= 1
            result[idx] += 1

cnt = 0
for k in result:
    if k >= 2:
        cnt += 1


print(cnt)