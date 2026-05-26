n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
result = [0 for _ in range(200)]
for i in segments: # (1, 5), (4, 6), ...
    start, end = min(i), max(i)
    for j in range(start+100, end+100):
        result[j] += 1

print(max(result))

