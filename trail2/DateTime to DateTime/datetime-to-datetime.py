a, b, c = map(int, input().split())

# Please write your code here.
# 0일부터 시작하기
start = 11 + (11 * 60) + (11 * 24 * 60)
end = c + (b * 60) + (a * 24 * 60)

result = end - start

if result < 0:
    print(-1)
else:
    print(end - start)