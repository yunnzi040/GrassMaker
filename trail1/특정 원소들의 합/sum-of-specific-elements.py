# 배열 4줄 입력받기
arr = [list(map(int, input().split())) for _ in range(4)]

# 색칠된 칸들에 해당하는 정수의 합
total = 0

for i in range(len(arr)):
    for j in range(i+1):
        total += arr[i][j]

print(total)