n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
result = [0 for _ in range(101)]

for i in segments:
    start, end = min(i), max(i)
    for j in range(start, end+1):
        result[j] += 1

print(max(result))
