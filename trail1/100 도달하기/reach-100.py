N = int(input())
arr = [1, N]

# 마지막 항이 100이 넘을 경우, 배열에 넣고 종료
while(arr[-1] < 100):
    arr.append(arr[-1] + arr[-2])

print(*arr)
