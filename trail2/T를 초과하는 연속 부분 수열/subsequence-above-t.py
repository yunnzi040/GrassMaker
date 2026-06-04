n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

max_cnt = 0
cnt = 0

for i in range(n):
    if arr[i] > t:
        cnt += 1
        max_cnt = max(max_cnt, cnt)
    else:
        cnt = 0

print(max_cnt)