row_avg = []
col_avg = [0,0,0,0]
all_avg = 0
count = 0

for _ in range (2):
    arr = list(map(int, input().split()))

    # 가로 평균
    row_avg.append(round(sum(arr) / len(arr), 1))

    for i in range(len(arr)):
        col_avg[i] += arr[i]
        all_avg += arr[i] # 전체 원소의 합
        count += 1 # 전체 원소 갯수

for i in range(len(col_avg)):
    col_avg[i] = col_avg[i] / 2


print(*row_avg)
print(*col_avg)
print(round(all_avg/count, 1))
